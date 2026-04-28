from gramatica_finalVisitor import gramatica_finalVisitor

class TACGenerator(gramatica_finalVisitor):
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
        self.current_function = None
        self.current_loop_labels = []  # Pila para break/continue
    
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"
    
    def add(self, instruction):
        self.instructions.append(instruction)
        return instruction
    
    def get_code(self):
        return "\n".join(self.instructions)
    
    #  VISITORS PRINCIPALES 
    
    def visitRoot(self, ctx):
        self.add("# Código TAC generado")
        for prog in ctx.programa():
            self.visit(prog)
        return self.get_code()
    
    def visitPrograma(self, ctx):
        if ctx.funcion():
            self.visit(ctx.funcion())
        elif ctx.declaracion():
            self.visit(ctx.declaracion())
        elif ctx.sentenciaGlobal():
            self.visit(ctx.sentenciaGlobal())
        elif ctx.cicloWhile():
            self.visit(ctx.cicloWhile())
        return None
    
    def visitSentenciaGlobal(self, ctx):
        if ctx.printt():
            self.visit(ctx.printt())
        elif ctx.asignacion():
            self.visit(ctx.asignacion())
        return None
    
    #  DECLARACIONES Y ASIGNACIONES 
    
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            if isinstance(valor, str) and valor.startswith('t'):
                self.add(f"{nombre} = {valor}")
            else:
                self.add(f"{nombre} = {valor}")
        return nombre
    
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        if isinstance(valor, str) and valor.startswith('t'):
            self.add(f"{nombre} = {valor}")
        else:
            self.add(f"{nombre} = {valor}")
        return valor
    
    #  FUNCIONES 
    
    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()
        self.current_function = nombre
        
        self.add(f"\n# Función {nombre}")
        self.add(f"begin_func {nombre}")
        
        # Parámetros
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                param_nombre = p.ID().getText()
                self.add(f"  param {param_nombre}")
        
        # Visitar cuerpo
        self.visit(ctx.bloque())
        
        self.add(f"end_func {nombre}")
        self.current_function = None
        return None
    
    def visitReturnStmt(self, ctx):
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            if isinstance(valor, str) and valor.startswith('t'):
                self.add(f"  return {valor}")
            else:
                self.add(f"  return {valor}")
        else:
            self.add(f"  return")
        return None
    
    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        args = []
        if ctx.argumentos():
            for arg in ctx.argumentos().expresion():
                arg_val = self.visit(arg)
                args.append(arg_val)
                self.add(f"  param {arg_val}")
        
        temp = self.new_temp()
        self.add(f"  {temp} = call {nombre}")
        return temp
    
    #  ESTRUCTURAS DE CONTROL 
    
    def visitExpresionSi(self, ctx):
        cond = self.visit(ctx.expresion())
        label_else = self.new_label()
        label_end = self.new_label()
        
        self.add(f"  if {cond} goto {label_else}")
        self.visit(ctx.bloque(0))
        self.add(f"  goto {label_end}")
        self.add(f"{label_else}:")
        
        if ctx.SINO():
            self.visit(ctx.bloque(1))
        
        self.add(f"{label_end}:")
        return None
    
    def visitCicloWhile(self, ctx):
        label_start = self.new_label()
        label_end = self.new_label()
        
        # Guardar labels para break/continue
        self.current_loop_labels.append((label_start, label_end))
        
        self.add(f"{label_start}:")
        cond = self.visit(ctx.expresion())
        self.add(f"  if {cond} goto {label_end}")
        self.visit(ctx.bloque())
        self.add(f"  goto {label_start}")
        self.add(f"{label_end}:")
        
        self.current_loop_labels.pop()
        return None
    
    # EXPRESIONES 
    
    def visitExpresion(self, ctx):
        return self.visit(ctx.comparacion())
    
    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.suma(i))
            temp = self.new_temp()
            
            if op == ">":
                self.add(f"  {temp} = {resultado} > {derecha}")
            elif op == "<":
                self.add(f"  {temp} = {resultado} < {derecha}")
            elif op == ">=":
                self.add(f"  {temp} = {resultado} >= {derecha}")
            elif op == "<=":
                self.add(f"  {temp} = {resultado} <= {derecha}")
            resultado = temp
        return resultado
    
    def visitSuma(self, ctx):
        resultado = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.termino(i))
            temp = self.new_temp()
            
            if op == "+":
                self.add(f"  {temp} = {resultado} + {derecha}")
            elif op == "-":
                self.add(f"  {temp} = {resultado} - {derecha}")
            resultado = temp
        return resultado
    
    def visitTermino(self, ctx):
        resultado = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.factor(i))
            temp = self.new_temp()
            
            if op == "*":
                self.add(f"  {temp} = {resultado} * {derecha}")
            elif op == "/":
                self.add(f"  {temp} = {resultado} / {derecha}")
            resultado = temp
        return resultado
    
    def visitFactor(self, ctx):
        if ctx.NUM():
            return ctx.NUM().getText()
        if ctx.STRING():
            return ctx.STRING().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        if ctx.expresion():
            return self.visit(ctx.expresion())
        return "0"
    
    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        self.add(f"  print {valor}")
        return None
    
    def visitBloque(self, ctx):
        for s in ctx.sentencia():
            self.visit(s)
        return None