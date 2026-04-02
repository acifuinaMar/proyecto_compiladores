from expresionVisitor import expresionVisitor

class Visitor(expresionVisitor):

    def __init__(self):
        self.memory = {}

    def visitRoot(self, ctx):
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)
        return resultado

    def visitSentencia(self, ctx):

        if ctx.asignacion():
            return self.visit(ctx.asignacion())

        if ctx.expresionSi():
            return self.visit(ctx.expresionSi())

        return self.visit(ctx.expresion())

    def visitAsignacion(self, ctx):

        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())

        self.memory[nombre] = valor
        return valor

    def visitExpresion(self, ctx):
        return self.visit(ctx.orLogico())

    def visitOrLogico(self, ctx):

        resultado = self.visit(ctx.andLogico(0))

        for i in range(1, len(ctx.andLogico())):
            resultado = resultado or self.visit(ctx.andLogico(i))

        return resultado

    def visitAndLogico(self, ctx):

        resultado = self.visit(ctx.igualdad(0))

        for i in range(1, len(ctx.igualdad())):
            resultado = resultado and self.visit(ctx.igualdad(i))

        return resultado

    def visitIgualdad(self, ctx):

        resultado = self.visit(ctx.comparacion(0))

        for i in range(1, len(ctx.comparacion())):

            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.comparacion(i))

            if op == "==":
                resultado = resultado == right
            elif op == "!=":
                resultado = resultado != right

        return resultado

    def visitComparacion(self, ctx):

        resultado = self.visit(ctx.suma(0))

        for i in range(1, len(ctx.suma())):

            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.suma(i))

            if op == ">":
                resultado = resultado > right
            elif op == "<":
                resultado = resultado < right
            elif op == ">=":
                resultado = resultado >= right
            elif op == "<=":
                resultado = resultado <= right

        return resultado

    def visitSuma(self, ctx):

        resultado = self.visit(ctx.multiplicacion(0))

        for i in range(1, len(ctx.multiplicacion())):

            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.multiplicacion(i))

            if op == "+":
                resultado = resultado + right
            elif op == "-":
                resultado = resultado - right

        return resultado

    def visitMultiplicacion(self, ctx):

        resultado = self.visit(ctx.unico(0))

        for i in range(1, len(ctx.unico())):

            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.unico(i))

            if op == "*":
                resultado = resultado * right
            elif op == "/":
                if right == 0:
                    raise Exception("División entre cero")
                resultado = resultado / right

        return resultado

    def visitUnico(self, ctx):

        if ctx.NOT():
            return not self.visit(ctx.unico())

        return self.visit(ctx.base())

    def visitBase(self, ctx):

        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.ID():
            nombre = ctx.ID().getText()

            if nombre not in self.memory:
                raise Exception(f"Variable '{nombre}' no definida")

            return self.memory[nombre]

        return self.visit(ctx.expresion())

    def visitExpresionSi(self, ctx):

        condicion = self.visit(ctx.expresion())

        if condicion:
            return self.visit(ctx.bloque(0))

        elif ctx.SINO():
            return self.visit(ctx.bloque(1))

        return None

    def visitBloque(self, ctx):

        resultado = None

        for s in ctx.sentencia():
            resultado = self.visit(s)

        return resultado