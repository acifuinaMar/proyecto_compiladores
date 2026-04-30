from gramatica_finalVisitor import gramatica_finalVisitor

class TACGenerator(gramatica_finalVisitor):
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
        self.loop_stack = []
    
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
    
    # FASE INICIAL: Corregido para usar 'programa'
    def visitRoot(self, ctx):
        self.add("# Código TAC generado")
        if ctx.programa():
            for p in ctx.programa():
                self.visit(p)
        return self.get_code()

    # NAVEGACIÓN DE REGLAS
    def visitPrograma(self, ctx): 
        return self.visitChildren(ctx)
    def visitSentenciaGlobal(self, ctx): 
        return self.visitChildren(ctx)

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()

        args = []
        if ctx.argumentos():
            args = [self.visit(e) for e in ctx.argumentos().expresion()]

        temp = self.new_temp()
        self.add(f"  {temp} = call {nombre}, {', '.join(args)}")
        return temp
    def visitBloque(self, ctx):
        if ctx.sentencia():
            for s in ctx.sentencia():
                self.visit(s)

    # EXPRESIONES: Corregido para pasar por 'comparacion'
    def visitExpresion(self, ctx):
        return self.visit(ctx.comparacion())

    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.suma(i))
            temp = self.new_temp()
            self.add(f"  {temp} = {resultado} {op} {derecha}")
            resultado = temp
        return resultado

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.termino(i))
            temp = self.new_temp()
            self.add(f"  {temp} = {resultado} {op} {derecha}")
            resultado = temp
        return resultado

    def visitTermino(self, ctx):
        resultado = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.factor(i))
            temp = self.new_temp()
            self.add(f"  {temp} = {resultado} {op} {derecha}")
            resultado = temp
        return resultado

    def visitFactor(self, ctx):
        if ctx.NUM():
            return ctx.NUM().getText()

        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.ID().getText()
            index = self.visit(ctx.expresion())

            temp = self.new_temp()
            self.add(f"  {temp} = {nombre}[{index}]")
            return temp

        if ctx.ID():
            return ctx.ID().getText()

        if ctx.PAI():
            return self.visit(ctx.expresion())

        return "0"

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()

        if ctx.arrayLiteral():
            valores = [self.visit(e) for e in ctx.arrayLiteral().expresion()]
            self.add(f"{nombre} = [{', '.join(valores)}]")
            return nombre

        valor = self.visit(ctx.expresion()) if ctx.expresion() else "0"
        self.add(f"{nombre} = {valor}")
        return nombre

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.add(f"{nombre} = {valor}")
        return valor

    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        self.add(f"  print {valor}")

    def visitExpresionSi(self, ctx):
        cond = self.visit(ctx.expresion())

        L_true = self.new_label()
        L_end = self.new_label()

        self.add(f"  if {cond} goto {L_true}")

        # else
        if ctx.SINO():
            self.visit(ctx.bloque(1))

        self.add(f"  goto {L_end}")

        # true
        self.add(f"{L_true}:")
        self.visit(ctx.bloque(0))

        self.add(f"{L_end}:")

    def visitCicloWhile(self, ctx):
        L_start = self.new_label()
        L_body = self.new_label()
        L_end = self.new_label()

        self.loop_stack.append((L_start, L_end))

        self.add(f"{L_start}:")
        cond = self.visit(ctx.expresion())
        self.add(f"  if {cond} goto {L_body}")
        self.add(f"  goto {L_end}")

        self.add(f"{L_body}:")
        self.visit(ctx.bloque())

        self.add(f"  goto {L_start}")

        self.add(f"{L_end}:")
        self.loop_stack.pop()

    def visitCicloFor(self, ctx):
        # init
        if ctx.declaracion():
            self.visit(ctx.declaracion())
        else:
            self.visit(ctx.asignacion(0))

        L_start = self.new_label()
        L_body = self.new_label()
        L_end = self.new_label()

        self.loop_stack.append((L_start, L_end))

        self.add(f"{L_start}:")
        cond = self.visit(ctx.expresion())
        self.add(f"  if {cond} goto {L_body}")
        self.add(f"  goto {L_end}")

        self.add(f"{L_body}:")
        self.visit(ctx.bloque())

        # update
        self.visit(ctx.asignacion()[-1])

        self.add(f"  goto {L_start}")
        self.add(f"{L_end}:")
        self.loop_stack.pop()

    def visitBreakStmt(self, ctx):
        if self.loop_stack:
            _, L_end = self.loop_stack[-1]
            self.add(f"  goto {L_end}")

    def visitContinueStmt(self, ctx):
        if self.loop_stack:
            L_start, _ = self.loop_stack[-1]
            self.add(f"  goto {L_start}")

    def visitFuncion(self, ctx):
        return None