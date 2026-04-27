from expresionVisitor import expresionVisitor

class Visitor(expresionVisitor):

    def __init__(self):
        self.scopes = [{}] 
        self.tabla_tipos = [{}] 
        self.funciones = [{}] #Como pila para poder anidar funciones
        self.current_function = None

    class ReturnException(Exception):
        def __init__(self, value):
            self.value = value

    def push_scope(self):
        """Crea un nuevo ámbito local (al entrar a un bloque {})"""
        self.scopes.append({})
        self.tabla_tipos.append({})
        self.funciones.append({})

    def get_funcion(self, nombre):
        for scope in reversed(self.funciones):
            if nombre in scope:
                return scope[nombre]
        return None

    def pop_scope(self):
        """Elimina el ámbito actual (al salir de un bloque {})"""
        self.scopes.pop()
        self.tabla_tipos.pop()
        self.funciones.pop()
        

    def get_var(self, nombre):
        """Busca una variable desde el ámbito más interno hacia el global"""
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]
        raise Exception(f"Error: La variable '{nombre}' no está definida")

    def set_var(self, nombre, valor):
        """Busca una variable existente y actualiza su valor"""
        for scope in reversed(self.scopes):
            if nombre in scope:
                scope[nombre] = valor
                return
        raise Exception(f"Error: No se puede asignar a '{nombre}' porque no ha sido declarada")

    def get_tipo_var(self, nombre):
        """Busca el tipo de una variable en la pila de tipos"""
        for t_scope in reversed(self.tabla_tipos):
            if nombre in t_scope:
                return t_scope[nombre]
        return None

    def visitRoot(self, ctx):
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)
        return resultado

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        tipo = ctx.TIPO().getText()
        valor = self.visit(ctx.expresion()) if ctx.expresion() else None

        if nombre in self.scopes[-1]:
            raise Exception(f"Error Semántico: La variable '{nombre}' ya existe en este ámbito local")

        self.tabla_tipos[-1][nombre] = tipo
        
        if valor is not None:
            if not self.validar_tipo(tipo, valor):
                raise Exception(f"Error de Tipo: '{nombre}' es {tipo} y no acepta {type(valor).__name__}")
            self.scopes[-1][nombre] = valor
        else:
            if tipo != "void":
                raise Exception(f"Error: No se puede asignar void a '{nombre}'")
                self.scopes[-1][nombre] = valor
                return valor

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        
        tipo_declarado = self.get_tipo_var(nombre)
        if not self.validar_tipo(tipo_declarado, valor):
            raise Exception(f"Error de Tipo: '{nombre}' espera {tipo_declarado}")

        self.set_var(nombre, valor)
        return valor

    def visitBloque(self, ctx):
        # Aquí ocurre el CONTROL DE ÁMBITOS
        self.push_scope() # PUSH
        
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)

        self.pop_scope() # POP
        return resultado

    def visitBase(self, ctx):
        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())

        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        if ctx.VERDADERO():
            return True

        if ctx.FALSO():
            return False

        if ctx.ID():
            nombre = ctx.ID().getText()
            return self.get_var(nombre)

        if ctx.expresion():
            return self.visit(ctx.expresion())

        return None

    def visitExpresionSi(self, ctx):
        condicion = self.visit(ctx.expresion())
        if condicion:
            return self.visit(ctx.bloque(0))
        elif ctx.SINO():
            return self.visit(ctx.bloque(1))
        return None

    def visitCicloWhile(self, ctx):
        while self.visit(ctx.expresion()):
            self.visit(ctx.bloque())
        return None
    def visitCicloFor(self, ctx): 
        if ctx.declaracion(): 
            self.visit(ctx.declaracion()) 
        else: 
            self.visit(ctx.asignacion(0)) 
        condicion = ctx.expresion() 
        actualizacion = ctx.asignacion()[-1] 
        
        while self.visit(condicion): 
            self.visit(ctx.bloque()) 
            self.visit(actualizacion) 
        return None

    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        print(valor)
        return valor

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.multiplicacion(0))
        for i in range(1, len(ctx.multiplicacion())):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.multiplicacion(i))
            if op == "+":
                if isinstance(resultado, str) or isinstance(right, str):
                    resultado = str(resultado) + str(right)
                else:
                    resultado = resultado + right   
            elif op == "-":
                resultado = resultado - right
        return resultado

    def visitMultiplicacion(self, ctx):
        resultado = self.visit(ctx.unico(0))
        for i in range(1, len(ctx.unico())):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.unico(i))
            if op == "*": resultado = resultado * right
            elif op == "/":
                if right == 0: raise Exception("División entre cero")
                resultado = resultado / right
        return resultado

    def visitUnico(self, ctx):
        if ctx.NOT(): return not self.visit(ctx.unico())
        return self.visit(ctx.base())

    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.suma(i))
            if op == ">": resultado = resultado > right
            elif op == "<": resultado = resultado < right
            elif op == ">=": resultado = resultado >= right
            elif op == "<=": resultado = resultado <= right
        return resultado

    def visitIgualdad(self, ctx):
        resultado = self.visit(ctx.comparacion(0))
        for i in range(1, len(ctx.comparacion())):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.comparacion(i))
            if op == "==": resultado = resultado == right
            elif op == "!=": resultado = resultado != right
        return resultado

    def visitAndLogico(self, ctx):
        resultado = self.visit(ctx.igualdad(0))
        for i in range(1, len(ctx.igualdad())):
            resultado = resultado and self.visit(ctx.igualdad(i))
        return resultado

    def visitOrLogico(self, ctx):
        resultado = self.visit(ctx.andLogico(0))
        for i in range(1, len(ctx.andLogico())):
            resultado = resultado or self.visit(ctx.andLogico(i))
        return resultado

    def visitExpresion(self, ctx):
        return self.visit(ctx.orLogico())

    def validar_tipo(self, tipo, valor):
        if tipo == "int": return isinstance(valor, int) and not isinstance(valor, bool)
        elif tipo == "float": return isinstance(valor, float)
        elif tipo == "string": return isinstance(valor, str)
        elif tipo == "bool": return isinstance(valor, bool)
        return False

    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()
        tipo = ctx.TIPO().getText()

        parametros = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                param_nombre = p.ID().getText()
                param_tipo = p.TIPO().getText()
                parametros.append((param_nombre, param_tipo))

        self.funciones[-1][nombre] = {
            "tipo": tipo,
            "parametros": parametros,
            "ctx": ctx
        }

        return None
    
    def visitReturnStmt(self, ctx):
        if self.current_function is None:
            raise Exception("Error: return fuera de función")

        if ctx.expresion():
            valor = self.visit(ctx.expresion())
        else:
            valor = None

        raise Visitor.ReturnException(valor)
    
    # Cuando llame una funcion:
    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        funcion = self.get_funcion(nombre)

        # argumentos
        argumentos = []
        if ctx.argumentos():
            for arg in ctx.argumentos().expresion():
                argumentos.append(self.visit(arg))

        # nuevo scope
        self.push_scope()

        # parametros
        for (param_nombre, param_tipo), valor in zip(funcion["parametros"], argumentos):
            self.scopes[-1][param_nombre] = valor
            self.tabla_tipos[-1][param_nombre] = param_tipo

        # ejecutar
        self.current_function = funcion
        retorno = None

        try:
            self.visit(funcion["ctx"].bloque())
        except Visitor.ReturnException as r:
            retorno = r.value

        # limpiar
        self.pop_scope()
        self.current_function = None

        # retorno limpio
        if funcion["tipo"] == "void":
            return None

        return retorno
