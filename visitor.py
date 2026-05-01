from gramatica_finalVisitor import gramatica_finalVisitor

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Visitor(gramatica_finalVisitor):

    def __init__(self):
        self.scopes = [{}]
        self.tabla_tipos = [{}]
        self.funciones = {}

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
        for p in ctx.programa():
            if p.funcion():
                self.visit(p.funcion())

        for p in ctx.programa():
            if not p.funcion():
                self.visit(p)

        return None

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()

        if ctx.arrayLiteral():
            valores = []
            for exp in ctx.arrayLiteral().expresion():
                valores.append(self.visit(exp))
            self.scopes[-1][nombre] = valores
            return None

        # normal
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
        return self.visit(ctx.comparacion())

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.termino(0))

        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i - 1).getText()
            derecha = self.visit(ctx.termino(i))

            print("SUMANDO:", resultado, op, derecha)  # debug

            if op == "+":
                resultado = resultado + derecha
            elif op == "-":
                resultado = resultado - derecha

        return resultado
        
    
    def visitComparacion(self, ctx):
        if len(ctx.suma()) == 1:
            return self.visit(ctx.suma(0))

        left = self.visit(ctx.suma(0))

        for i in range(1, len(ctx.suma())):
            right = self.visit(ctx.suma(i))
            op = ctx.getChild(2*i - 1).getText()

            if op == '<=':
                return left <= right
            elif op == '>=':
                return left >= right
            elif op == '<':
                return left < right
            elif op == '>':
                return left > right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right

        return False

    def visitTermino(self, ctx):
        resultado = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i - 1).getText()
            derecha = self.visit(ctx.factor(i))

            if op == "*":
                resultado *= derecha
            elif op == "/":
                resultado /= derecha
            elif op == "%":
                resultado %= derecha

        return resultado

    def visitFactor(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())

        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.ID().getText()
            index = self.visit(ctx.expresion())

            arr = self.get_var(nombre)

            if not isinstance(arr, list):
                raise Exception(f"'{nombre}' no es un arreglo")

            return arr[index]

        if ctx.ID():
            return self.get_var(ctx.ID().getText())

        if ctx.PAI():
            return self.visit(ctx.expresion())

        return 0

    def visitBloque(self, ctx):
        self.push_scope()
        try:
            for s in ctx.sentencia():
                self.visit(s)
        finally:
            self.pop_scope()
        return None
    
    def visitBreakStmt(self, ctx):
        raise BreakException()

    def visitContinueStmt(self, ctx):
        raise ContinueException()
    
    def visitCicloWhile(self, ctx):
        while self.visit(ctx.expresion()):
            try:
                self.visit(ctx.bloque())
            except BreakException:
                break
            except ContinueException:
                continue
        return None
    
    def visitCicloFor(self, ctx):
        # inicialización
        if ctx.declaracion():
            self.visit(ctx.declaracion())
        else:
            self.visit(ctx.asignacion(0))

        while self.visit(ctx.expresion()):
            try:
                self.visit(ctx.bloque())
            except BreakException:
                break
            except ContinueException:
                pass

            # actualización
            self.visit(ctx.asignacion()[-1])

        return None
    
    def visitExpresionSi(self, ctx):
        condicion = self.visit(ctx.expresion())

        if condicion:
            self.visit(ctx.bloque(0))
        elif ctx.SINO():
            self.visit(ctx.bloque(1))

        return None
    
    def visitCicloFor(self, ctx):
        # inicialización
        if ctx.declaracion():
            self.visit(ctx.declaracion())
        else:
            self.visit(ctx.asignacion(0))

        while self.visit(ctx.expresion()):
            try:
                self.visit(ctx.bloque())
            except BreakException:
                break
            except ContinueException:
                pass

            # actualización
            self.visit(ctx.asignacion()[-1])

        return None
    
    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()
        self.funciones[nombre] = ctx
        return None
    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()

        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida")

        funcion_ctx = self.funciones[nombre]
        self.push_scope()

        params = funcion_ctx.parametros().parametro() if funcion_ctx.parametros() else []
        args = ctx.argumentos().expresion() if ctx.argumentos() else []

        if len(args) != len(params):
            raise Exception(f"La función '{nombre}' esperaba {len(params)} argumentos pero recibió {len(args)}")

        for i in range(len(params)):
            nombre_param = params[i].ID().getText()
            valor_arg = self.visit(args[i])
            self.scopes[-1][nombre_param] = valor_arg

        resultado = None

        try:
            self.visit(funcion_ctx.bloque())
        except ReturnException as r:
            resultado = r.value

        self.pop_scope()

        if resultado is None:
            raise Exception(f"La función '{nombre}' no retornó ningún valor")

        return resultado
            
    def visitReturnStmt(self, ctx):
        valor = self.visit(ctx.expresion()) if ctx.expresion() else None
        print("RETURN:", valor)
        raise ReturnException(valor)
