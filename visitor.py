from expresionVisitor import expresionVisitor

class Visitor(expresionVisitor):

    def __init__(self):
        # Inciso 5: Pila de Ámbitos usando una lista de diccionarios (Tablas Hash)
        # El índice 0 siempre será el ámbito GLOBAL.
        self.scopes = [{}] 
        self.tabla_tipos = [{}] 

    # --- FUNCIONES DE APOYO (HELPERS) PARA ÁMBITOS ---
    
    def push_scope(self):
        """Crea un nuevo ámbito local (al entrar a un bloque {})"""
        self.scopes.append({})
        self.tabla_tipos.append({})

    def pop_scope(self):
        """Elimina el ámbito actual (al salir de un bloque {})"""
        self.scopes.pop()
        self.tabla_tipos.pop()

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

    # --- MÉTODOS VISITORS ---

    def visitRoot(self, ctx):
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)
        return resultado

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        tipo = ctx.TIPO().getText()
        valor = self.visit(ctx.expresion()) if ctx.expresion() else None

        # Shadowing y Error de Duplicados:
        # Revisamos SOLO el ámbito actual (el tope de la pila: index -1)
        if nombre in self.scopes[-1]:
            raise Exception(f"Error Semántico: La variable '{nombre}' ya existe en este ámbito local")

        # Guardamos tipo y valor en el ámbito actual
        self.tabla_tipos[-1][nombre] = tipo
        
        if valor is not None:
            if not self.validar_tipo(tipo, valor):
                raise Exception(f"Error de Tipo: '{nombre}' es {tipo} y no acepta {type(valor).__name__}")

        self.scopes[-1][nombre] = valor
        return valor

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        
        # Validamos tipo antes de actualizar
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
        if ctx.NUM(): return int(ctx.NUM().getText())
        if ctx.FLOAT(): return float(ctx.FLOAT().getText())
        if ctx.STRING(): return ctx.STRING().getText().strip('"')
        if ctx.VERDADERO(): return True
        if ctx.FALSO(): return False
        
        if ctx.ID():
            nombre = ctx.ID().getText()
            return self.get_var(nombre) # Busca en la pila
            
        return self.visit(ctx.expresion())

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

    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        print(valor)
        return valor

    # --- LÓGICA ARITMÉTICA Y LOGICA ---

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