from gramatica_finalVisitor import gramatica_finalVisitor

class TACGenerator(gramatica_finalVisitor):
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
    
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
    
    def visitRoot(self, ctx):
        self.add("# Código TAC generado")
        for s in ctx.sentencia():
            self.visit(s)
        return self.get_code()
    
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self.add(f"{nombre} = {valor}")
        else:
            self.add(f"{nombre} = 0")
        return nombre
    
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.add(f"{nombre} = {valor}")
        return valor
    
    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        self.add(f"  print {valor}")
        return None
    
    def visitExpresion(self, ctx):
        return self.visit(ctx.suma())
    
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
            elif op == "%":
                self.add(f"  {temp} = {resultado} % {derecha}")
            resultado = temp
        return resultado
    
    def visitFactor(self, ctx):
        if ctx.NUM():
            return ctx.NUM().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.PAI():
            return self.visit(ctx.expresion())
        return "0"
    
    def visitBloque(self, ctx):
        for s in ctx.sentencia():
            self.visit(s)
        return None
