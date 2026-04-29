from gramatica_finalVisitor import gramatica_finalVisitor

class Visitor(gramatica_finalVisitor):

    def __init__(self):
        self.scopes = [{}]
        self.tabla_tipos = [{}]

    def push_scope(self):
        self.scopes.append({})
        self.tabla_tipos.append({})

    def pop_scope(self):
        self.scopes.pop()
        self.tabla_tipos.pop()

    def get_var(self, nombre):
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]
        raise Exception(f"Variable '{nombre}' no definida")

    def set_var(self, nombre, valor):
        for scope in reversed(self.scopes):
            if nombre in scope:
                scope[nombre] = valor
                return
        raise Exception(f"Variable '{nombre}' no declarada")

    def visitRoot(self, ctx):
        for child in ctx.getChildren():
            self.visit(child)
        return None

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self.scopes[-1][nombre] = valor
        else:
            self.scopes[-1][nombre] = 0
        return None

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.set_var(nombre, valor)
        return valor

    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        print(valor)
        return None

    def visitExpresion(self, ctx):
        return self.visit(ctx.suma())

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.termino(i))
            if op == "+":
                resultado = resultado + derecha
            elif op == "-":
                resultado = resultado - derecha
        return resultado

    def visitTermino(self, ctx):
        resultado = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.factor(i))
            if op == "*":
                resultado = resultado * derecha
            elif op == "/":
                resultado = resultado / derecha
            elif op == "%":
                resultado = resultado % derecha
        return resultado

    def visitFactor(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        if ctx.ID():
            return self.get_var(ctx.ID().getText())
        if ctx.PAI():
            return self.visit(ctx.expresion())
        return 0

    def visitBloque(self, ctx):
        self.push_scope()
        for s in ctx.sentencia():
            self.visit(s)
        self.pop_scope()
        return None
