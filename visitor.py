from expresionVisitor import expresionVisitor

class Visitor(expresionVisitor):

    def __init__(self):
        self.memory = {}

    # program { sentencia* }
    def visitRoot(self, ctx):

        resultado = None

        for s in ctx.sentencia():
            resultado = self.visit(s)

        return resultado


    # sentencia puede ser asignacion | expresion
    def visitSentencia(self, ctx):

        if ctx.asignacion():
            return self.visit(ctx.asignacion())

        return self.visit(ctx.expresion())


    # asignación de variables
    def visitAsignacion(self, ctx):

        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())

        self.memory[nombre] = valor

        return valor


    def visitExpresion(self, ctx):
        return self.visit(ctx.orLogico())


    # o lógico
    def visitOrLogico(self, ctx):

        resultado = self.visit(ctx.andLogico(0))

        for i in range(1, len(ctx.andLogico())):
            resultado = resultado or self.visit(ctx.andLogico(i))

        return resultado


    # y Logico
    def visitAndLogico(self, ctx):

        resultado = self.visit(ctx.igualdad(0))

        for i in range(1, len(ctx.igualdad())):
            resultado = resultado and self.visit(ctx.igualdad(i))

        return resultado


    # Igualdades
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


    # Comparación
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


    # Suma o resta
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


    # Multiplicación o división
    def visitMultiplicacion(self, ctx):

        resultado = self.visit(ctx.unico(0))

        for i in range(1, len(ctx.unico())):

            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.unico(i))

            if op == "*":
                resultado = resultado * right
            elif op == "/":
                resultado = resultado / right

        return resultado


    # negacióoon
    def visitUnico(self, ctx):

        if ctx.NOT():
            return not self.visit(ctx.unico())

        return self.visit(ctx.base())


    # unidades básicas
    def visitBase(self, ctx):

        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.ID():
            nombre = ctx.ID().getText()
            return self.memory.get(nombre, 0)

        if ctx.expresion():
            return self.visit(ctx.expresion())

        if ctx.expresionSi():
            return self.visit(ctx.expresionSi())


    # condicional si
    def visitExpresionSi(self, ctx):

        condicion = self.visit(ctx.expresion(0))

        if condicion:
            return self.visit(ctx.expresion(1))

        if ctx.SINO():
            return self.visit(ctx.expresion(2))

        return None