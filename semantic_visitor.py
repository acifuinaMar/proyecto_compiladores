from expresionVisitor import expresionVisitor

class SemanticVisitor(expresionVisitor):

    def __init__(self):
        self.tabla_tipos = [{}] 
        self.errores = []

    def push_scope(self):
        self.tabla_tipos.append({})

    def pop_scope(self):
        self.tabla_tipos.pop()

    def get_tipo_var(self, nombre):
        """Busca el tipo de una variable desde el ámbito local al global"""
        for t_scope in reversed(self.tabla_tipos):
            if nombre in t_scope:
                return t_scope[nombre]
        return None

    def registrar_error(self, ctx, mensaje):
        """Reporta error con línea y columna exacta"""
        linea = ctx.start.line
        columna = ctx.start.column
        self.errores.append(f"[Error Semántico] Línea {linea}, Columna {columna}: {mensaje}")

    def visitRoot(self, ctx):
        for s in ctx.sentencia():
            self.visit(s)
        return self.errores

    def visitBloque(self, ctx):
        for s in ctx.sentencia():
            self.visit(s)
        return None

    def visitFuncion(self, ctx):
        """Paso crítico: Registra parámetros antes de validar el cuerpo"""
        nombre_func = ctx.ID().getText()
        tipo_retorno = ctx.TIPO().getText()
        
        self.tabla_tipos[0][nombre_func] = tipo_retorno 

        self.push_scope() 
        
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                p_nombre = p.ID().getText()
                p_tipo = p.TIPO().getText()
                self.tabla_tipos[-1][p_nombre] = p_tipo
        
        self.visit(ctx.bloque())
        
        self.pop_scope()
        return None

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        tipo = ctx.TIPO().getText()
        
        if nombre in self.tabla_tipos[-1]: 
            self.registrar_error(ctx, f"La variable '{nombre}' ya ha sido declarada en este nivel.")
        else:
            self.tabla_tipos[-1][nombre] = tipo
            
        if ctx.expresion():
            self.visit(ctx.expresion())
        return tipo

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        tipo_declarado = self.get_tipo_var(nombre)
        
        if not tipo_declarado:
            self.registrar_error(ctx, f"La variable '{nombre}' no ha sido declarada.")
            return None

        tipo_valor = self.visit(ctx.expresion())
        
        if not tipo_valor:
            return tipo_declarado 

        if tipo_declarado != tipo_valor:
            if not (tipo_declarado == "float" and tipo_valor == "int"):
                self.registrar_error(ctx, f"Incompatibilidad: '{nombre}' es {tipo_declarado} y recibio {tipo_valor}")
        
        return tipo_declarado

    def visitCicloWhile(self, ctx):
        if self.visit(ctx.expresion()) != "bool":
            self.registrar_error(ctx, "Condición de while debe ser bool.")
        self.push_scope()
        self.visit(ctx.bloque())
        self.pop_scope()
        return None

    def visitLlamadaFuncion(self, ctx):
        """Valida que la función llamada exista"""
        nombre = ctx.ID().getText()
        tipo = self.get_tipo_var(nombre)
        if not tipo:
            self.registrar_error(ctx, f"Función '{nombre}' no definida.")
        return "int"

    def visitBase(self, ctx):
        if ctx.ID():
            nombre = ctx.ID().getText()
            tipo = self.get_tipo_var(nombre)
            if not tipo:
                self.registrar_error(ctx, f"La variable '{nombre}' no está definida.")
                return "int"
            return tipo
        if ctx.NUM(): return "int"
        if ctx.FLOAT(): return "float"
        if ctx.STRING(): return "string"
        if ctx.VERDADERO() or ctx.FALSO(): return "bool"
        if ctx.expresion(): return self.visit(ctx.expresion())
        if hasattr(ctx, 'llamadaFuncion') and ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        return "void"

    def visitSuma(self, ctx):
        tipo = self.visit(ctx.multiplicacion(0))
        for i in range(1, len(ctx.multiplicacion())):
            t_sig = self.visit(ctx.multiplicacion(i))
            if tipo == "string" or t_sig == "string":
                tipo = "string"
            elif tipo == "float" or t_sig == "float":
                tipo = "float"
            else:
                tipo = "int"
        return tipo

    def visitPrintt(self, ctx):
        self.visit(ctx.expresion())
        return None
    
    def visitReturnStmt(self, ctx):
        if ctx.expresion():
            return self.visit(ctx.expresion())
        return "void"
    
    def visitFuncion(self, ctx):
        nombre_func = ctx.ID().getText()
        tipo_retorno = ctx.TIPO().getText()
        
        self.tabla_tipos[0][nombre_func] = {"tipo": tipo_retorno}
        
        self.push_scope()
        
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                p_nombre = p.ID().getText()
                p_tipo = p.TIPO().getText()
                self.tabla_tipos[-1][p_nombre] = p_tipo
        
        self.visit(ctx.bloque())
        
        self.pop_scope()
        return None

    def visitParametro(self, ctx):
        tipo = ctx.TIPO().getText()
        nombre = ctx.ID().getText()
        self.tabla_tipos[-1][nombre] = tipo
        return tipo

    def visitReturnStmt(self, ctx):
        if ctx.expresion():
            return self.visit(ctx.expresion())
        return "void"

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        func_info = self.tabla_tipos[0].get(nombre)
        if not func_info:
            self.registrar_error(ctx, f"La función '{nombre}' no ha sido definida.")
            return "int"
        return func_info["tipo"]
    
    def visitParametro(self, ctx):
        tipo = ctx.TIPO().getText()
        nombre = ctx.ID().getText()
        self.tabla_tipos[-1][nombre] = tipo
        return tipo
    
    def visitOrLogico(self, ctx):
        for i in range(len(ctx.andLogico())):
            self.visit(ctx.andLogico(i))
        return "bool"

    def visitAndLogico(self, ctx):
        for i in range(len(ctx.igualdad())):
            self.visit(ctx.igualdad(i))
        return "bool"

    def visitIgualdad(self, ctx):
        for i in range(len(ctx.comparacion())):
            self.visit(ctx.comparacion(i))
        return "bool"

    def visitComparacion(self, ctx):
        for i in range(len(ctx.suma())):
            self.visit(ctx.suma(i))
        return "bool"
    
    def visitMultiplicacion(self, ctx):
        tipo = self.visit(ctx.unico(0))
        for i in range(1, len(ctx.unico())):
            t_sig = self.visit(ctx.unico(i))
            if tipo == "float" or t_sig == "float":
                tipo = "float"
            else:
                tipo = "int"
        return tipo

    def visitUnico(self, ctx):
        if ctx.NOT():
            self.visit(ctx.unico())
            return "bool"
        return self.visit(ctx.base())
    
    def visitMultiplicacion(self, ctx):
        tipo = self.visit(ctx.unico(0))
        for i in range(1, len(ctx.unico())):
            t_sig = self.visit(ctx.unico(i))
            if tipo == "float" or t_sig == "float":
                tipo = "float"
            else:
                tipo = "int"
        return tipo

    def visitUnico(self, ctx):
        if ctx.NOT():
            self.visit(ctx.unico())
            return "bool"
        return self.visit(ctx.base())

    def visitOrLogico(self, ctx):
        tipo = self.visit(ctx.andLogico(0))
        if len(ctx.andLogico()) > 1:
            for i in range(1, len(ctx.andLogico())):
                self.visit(ctx.andLogico(i))
            return "bool"
        return tipo

    def visitAndLogico(self, ctx):
        tipo = self.visit(ctx.igualdad(0))
        if len(ctx.igualdad()) > 1:
            for i in range(1, len(ctx.igualdad())):
                self.visit(ctx.igualdad(i))
            return "bool"
        return tipo

    def visitIgualdad(self, ctx):
        tipo = self.visit(ctx.comparacion(0))
        if len(ctx.comparacion()) > 1:
            for i in range(1, len(ctx.comparacion())):
                self.visit(ctx.comparacion(i))
            return "bool"
        return tipo

    def visitComparacion(self, ctx):
        tipo = self.visit(ctx.suma(0))
        if len(ctx.suma()) > 1:
            for i in range(1, len(ctx.suma())):
                self.visit(ctx.suma(i))
            return "bool"
        return tipo
