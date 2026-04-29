from gramatica_finalVisitor import gramatica_finalVisitor

class TACGenerator(gramatica_finalVisitor):
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
    
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
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
    def visitPrograma(self, ctx): return self.visitChildren(ctx)
    def visitSentenciaGlobal(self, ctx): return self.visitChildren(ctx)

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
        if ctx.NUM(): return ctx.NUM().getText()
        if ctx.ID(): return ctx.ID().getText()
        if ctx.PAI(): return self.visit(ctx.expresion())
        return "0"

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
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
