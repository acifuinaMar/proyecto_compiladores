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
        self.structs = {}

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
        if len(ctx.ID()) == 2:

            tipo_struct = ctx.ID(0).getText()
            nombre_var = ctx.ID(1).getText()

            if tipo_struct in self.structs:

                self.scopes[-1][nombre_var] = self.structs[tipo_struct].copy()
                
                return None
            
        nombre = ctx.ID()[0].getText()

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
        # p.x = valor
        if ctx.getChildCount() >= 5 and ctx.getChild(1).getText() == ".":
            nombre_struct = ctx.ID(0).getText()
            campo = ctx.ID(1).getText()
            valor = self.visit(ctx.expresion(0))

            instancia = self.get_var(nombre_struct)

            if not isinstance(instancia, dict):
                raise Exception(f"'{nombre_struct}' no es un struct")

            instancia[campo] = valor

            return valor

        # nums[i] = valor
        if ctx.CORI():
            nombre = ctx.ID(0).getText()
            arreglo = self.get_var(nombre)
            indice = self.visit(ctx.expresion(0))
            valor = self.visit(ctx.expresion(1))
            arreglo[indice] = valor
            return valor

        # normal
        nombre = ctx.ID(0).getText()
        valor = self.visit(ctx.expresion(0))

        self.set_var(nombre, valor)
        return valor

    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        print(valor)
        return None

    def visitExpresion(self, ctx):
        condicion = self.visit(ctx.comparacion())
        # ternario
        if ctx.getChildCount() > 1:
            verdadero = self.visit(ctx.expresion(0))
            falso = self.visit(ctx.expresion(1))
            return verdadero if condicion else falso
        return condicion

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.termino(0))

        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i - 1).getText()
            derecha = self.visit(ctx.termino(i))

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
            nombre = ctx.ID(0).getText()
            index = self.visit(ctx.expresion())

            arr = self.get_var(nombre)

            if not isinstance(arr, list):
                raise Exception(f"'{nombre}' no es un arreglo")

            return arr[index]
        
        # acceso struct p.x
        if len(ctx.ID()) == 2:
            nombre_struct = ctx.ID(0).getText()
            campo = ctx.ID(1).getText()

            instancia = self.get_var(nombre_struct)
            if not isinstance(instancia, dict):
                raise Exception(f"'{nombre_struct}' no es un struct")

            return instancia[campo]

        if len(ctx.ID()) == 1:
            return self.get_var(ctx.ID(0).getText())

        if ctx.TIPO():
            tipo_destino = ctx.TIPO().getText()

            valor = self.visit(ctx.factor())

            if tipo_destino == "int":
                return int(valor)

            elif tipo_destino == "float":
                return float(valor)

            elif tipo_destino == "string":
                return str(valor)

            return valor
        
        if ctx.PAI():
            return self.visit(ctx.expresion())
        
        if ctx.RES():
            return -self.visit(ctx.factor())

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
    
    def visitSwitchStmt(self, ctx):
        valor_switch = self.visit(ctx.expresion())
        ejecutado = False

        for case_ctx in ctx.caseStmt():
            valor_case = int(case_ctx.NUM().getText())
            if valor_switch == valor_case:
                ejecutado = True
                try:
                    for s in case_ctx.sentencia():
                        self.visit(s)
                except BreakException:
                    pass
                return None

        # default
        if not ejecutado and ctx.defaultStmt():
            for s in ctx.defaultStmt().sentencia():
                self.visit(s)
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
        raise ReturnException(valor)
    
    def visitStructDecl(self, ctx):
        nombre_struct = ctx.ID().getText()
        campos = {}

        for campo in ctx.campoStruct():
            nombre_campo = campo.ID().getText()
            campos[nombre_campo] = 0
        self.structs[nombre_struct] = campos
        

        return None
