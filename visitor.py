from expresionVisitor import expresionVisitor

class Visitor(expresionVisitor):

    def __init__(self):
        self.memory = {}
        self.tabla_tipos = {}
        self.memory = {}
    
    def visitRoot(self, ctx):
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)
        return resultado

    def visitSentencia(self, ctx):
        if ctx.declaracion():
            return self.visit(ctx.declaracion())

        if ctx.asignacion():
            return self.visit(ctx.asignacion())

        if ctx.expresionSi():
            return self.visit(ctx.expresionSi())

        if ctx.printt():
            return self.visit(ctx.printt())
        
        if ctx.cicloWhile():
            return self.visit(ctx.cicloWhile())
        
        if ctx.cicloFor():
            return self.visit(ctx.cicloFor())

        if ctx.expresion():
            return self.visit(ctx.expresion())

        return None

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())

        tipo = self.tabla_tipos.get(nombre)

        if tipo is None:
            raise Exception(f"Variable {nombre} no declarada")

        if not self.validar_tipo(tipo, valor):
            raise Exception(f"Error de tipo: {nombre} es {tipo} y recibe {type(valor).__name__}")

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
    
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        tipo = ctx.TIPO().getText()

        valor = self.visit(ctx.expresion()) if ctx.expresion() else None

        # Guardar tipo
        self.tabla_tipos[nombre] = tipo

        # Validar tipo
        if valor is not None:
            if not self.validar_tipo(tipo, valor):
                raise Exception(f"Error de tipo: no se puede asignar {type(valor).__name__} a {tipo}")

        # Guardar valor
        self.memory[nombre] = valor

        return valor
    
    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        print(valor)
        return valor
    
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
    
    def validar_tipo(self, tipo, valor):
        if tipo == "int":
            return isinstance(valor, int) and not isinstance(valor, bool)

        elif tipo == "float":
            return isinstance(valor, float)

        elif tipo == "string":
            return isinstance(valor, str)

        elif tipo == "bool":
            return isinstance(valor, bool)

        return False