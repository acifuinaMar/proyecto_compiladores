# visitor.py - Versión actualizada para la nueva gramática
from gramatica_finalVisitor import gramatica_finalVisitor

class Visitor(gramatica_finalVisitor):

    def __init__(self):
        self.scopes = [{}]      # Pila de valores
        self.tabla_tipos = [{}] # Pila de tipos
        self.funciones = {}     # Diccionario GLOBAL de funciones
        self.current_function = None
        self.current_return_type = None

    class ReturnException(Exception):
        def __init__(self, value):
            self.value = value

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

    def get_tipo(self, nombre):
        for t_scope in reversed(self.tabla_tipos):
            if nombre in t_scope:
                return t_scope[nombre]
        return None

    def validar_tipo(self, tipo, valor):
        if tipo == "int":
            return isinstance(valor, int) and not isinstance(valor, bool)
        elif tipo == "float":
            return isinstance(valor, (int, float))
        elif tipo == "string":
            return isinstance(valor, str)
        elif tipo == "bool":
            return isinstance(valor, bool)
        return False

    def visitRoot(self, ctx):
        resultado = None
        for prog in ctx.programa():
            resultado = self.visit(prog)
        return resultado

    def visitPrograma(self, ctx):
        # Programa puede ser funcion, declaracion, sentenciaGlobal o cicloWhile
        if ctx.funcion():
            return self.visit(ctx.funcion())
        elif ctx.declaracion():
            return self.visit(ctx.declaracion())
        elif ctx.sentenciaGlobal():
            return self.visit(ctx.sentenciaGlobal())
        elif ctx.cicloWhile():
            return self.visit(ctx.cicloWhile())
        return None

    def visitSentenciaGlobal(self, ctx):
        if ctx.printt():
            return self.visit(ctx.printt())
        elif ctx.asignacion():
            return self.visit(ctx.asignacion())
        return None

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        tipo = ctx.TIPO().getText()
        valor = self.visit(ctx.expresion()) if ctx.expresion() else None
        
        if nombre in self.scopes[-1]:
            raise Exception(f"Variable '{nombre}' ya declarada en este ámbito")
        
        self.tabla_tipos[-1][nombre] = tipo
        
        if valor is not None:
            if not self.validar_tipo(tipo, valor):
                raise Exception(f"Tipo incorrecto para '{nombre}': espera {tipo}")
            self.scopes[-1][nombre] = valor
        else:
            if tipo == "int":
                self.scopes[-1][nombre] = 0
            elif tipo == "float":
                self.scopes[-1][nombre] = 0.0
            elif tipo == "bool":
                self.scopes[-1][nombre] = False
            elif tipo == "string":
                self.scopes[-1][nombre] = ""
        
        return None

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        
        encontrada = False
        for scope in reversed(self.scopes):
            if nombre in scope:
                scope[nombre] = valor
                encontrada = True
                break
        
        if not encontrada:
            raise Exception(f"Variable '{nombre}' no declarada")
        
        return valor

    def visitBloque(self, ctx):
        self.push_scope()
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)
        self.pop_scope()
        return resultado

    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()
        tipo_retorno = ctx.TIPO().getText()
        
        parametros = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                param_nombre = p.ID().getText()
                param_tipo = p.TIPO().getText()
                parametros.append((param_nombre, param_tipo))
        
        self.funciones[nombre] = {
            "tipo": tipo_retorno,
            "parametros": parametros,
            "ctx": ctx
        }
        return None

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        
        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida")
        
        funcion = self.funciones[nombre]
        
        argumentos = []
        if ctx.argumentos():
            for arg in ctx.argumentos().expresion():
                argumentos.append(self.visit(arg))
        
        if len(argumentos) != len(funcion["parametros"]):
            raise Exception(f"Función '{nombre}' espera {len(funcion['parametros'])} argumentos, recibe {len(argumentos)}")
        
        self.push_scope()
        
        for (param_nombre, param_tipo), arg_valor in zip(funcion["parametros"], argumentos):
            self.tabla_tipos[-1][param_nombre] = param_tipo
            self.scopes[-1][param_nombre] = arg_valor
        
        old_function = self.current_function
        old_return_type = self.current_return_type
        self.current_function = nombre
        self.current_return_type = funcion["tipo"]
        
        retorno = None
        try:
            self.visit(funcion["ctx"].bloque())
        except self.ReturnException as r:
            retorno = r.value
        
        self.pop_scope()
        self.current_function = old_function
        self.current_return_type = old_return_type
        
        return retorno

    def visitReturnStmt(self, ctx):
        if self.current_function is None:
            raise Exception("Return fuera de función")
        
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            if not self.validar_tipo(self.current_return_type, valor):
                raise Exception(f"Return espera {self.current_return_type}, devuelve {type(valor).__name__}")
        else:
            if self.current_return_type != "void":
                raise Exception(f"Función {self.current_return_type} debe retornar un valor")
            valor = None
        
        raise self.ReturnException(valor)

    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        print(valor)
        return valor

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
        
        while self.visit(ctx.expresion()):
            self.visit(ctx.bloque())
            self.visit(ctx.asignacion()[-1])
        return None
    
    def visitExpresion(self, ctx):
        return self.visit(ctx.comparacion())
    
    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.suma(i))
            if op == ">":
                resultado = resultado > derecha
            elif op == "<":
                resultado = resultado < derecha
            elif op == ">=":
                resultado = resultado >= derecha
            elif op == "<=":
                resultado = resultado <= derecha
        return resultado
    
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
                if derecha == 0:
                    raise Exception("División entre cero")
                resultado = resultado / derecha
        return resultado
    
    def visitFactor(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        if ctx.ID():
            return self.get_var(ctx.ID().getText())
        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        if ctx.expresion():
            return self.visit(ctx.expresion())
        if ctx.NOT():
            return not self.visit(ctx.factor())
        return 0