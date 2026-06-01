# semantic_visitor.py - Versión corregida
from gramatica_finalVisitor import gramatica_finalVisitor

class SemanticVisitor(gramatica_finalVisitor):

    def __init__(self):
        self.tabla_tipos = [{}] 
        self.errores = []
        self.en_ciclo = 0

    def push_scope(self):
        self.tabla_tipos.append({})

    def pop_scope(self):
        self.tabla_tipos.pop()

    def get_tipo_var(self, nombre):
        for t_scope in reversed(self.tabla_tipos):
            if nombre in t_scope:
                return t_scope[nombre]
        return None

    def registrar_error(self, ctx, mensaje):
        linea = ctx.start.line
        columna = ctx.start.column
        self.errores.append(f"[Error Semántico] Línea {linea}, Columna {columna}: {mensaje}")

    def visitRoot(self, ctx):
        for prog in ctx.programa():
            self.visit(prog)
        return self.errores

    def visitBloque(self, ctx):
        self.push_scope()
        for s in ctx.sentencia():
            self.visit(s)
        self.pop_scope()
        return None

    def visitFuncion(self, ctx):
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
        ids = ctx.ID()

        # Declaración de struct:s
        if len(ids) == 2:

            tipo = ids[0].getText()
            nombre = ids[1].getText()

            if nombre in self.tabla_tipos[-1]:
                self.registrar_error(
                    ctx,
                    f"Variable '{nombre}' ya declarada en este ámbito"
                )
            else:
                self.tabla_tipos[-1][nombre] = tipo

            return tipo

        # Declaraciones normales
        nombre = ids[0].getText()
        tipo = ctx.TIPO().getText()

        # detectar array
        if ctx.CORI():
            tipo = tipo + "[]"

        if nombre in self.tabla_tipos[-1]:
            self.registrar_error(
                ctx,
                f"Variable '{nombre}' ya declarada en este ámbito"
            )
        else:
            self.tabla_tipos[-1][nombre] = tipo

        # validar asignación
        if ctx.expresion():
            tipo_exp = self.visit(ctx.expresion())

            if tipo and tipo_exp and tipo != tipo_exp:
                if not (tipo == "float" and tipo_exp == "int"):
                    self.registrar_error(
                        ctx,
                        f"Incompatibilidad: '{nombre}' es {tipo} y recibe {tipo_exp}"
                    )

        return tipo

    def visitAsignacion(self, ctx):
        if len(ctx.ID()) == 2:
            nombre_struct = ctx.ID(0).getText()
            campo = ctx.ID(1).getText()
            tipo_struct = self.get_tipo_var(nombre_struct)

            if not tipo_struct:
                self.registrar_error(
                    ctx,
                    f"Variable '{nombre_struct}' no ha sido declarada"
                )
                return None
            return "int"   # temporal

        # arreglo[index] = valor
        if ctx.CORI():
            nombre = ctx.ID(0).getText()
            tipo = self.get_tipo_var(nombre)
            if not tipo:
                self.registrar_error(
                    ctx,
                    f"Arreglo '{nombre}' no declarado"
                )
                return None
            return tipo

        # normal
        nombre = ctx.ID(0).getText()

        tipo_declarado = self.get_tipo_var(nombre)
        if not tipo_declarado:
            self.registrar_error(
                ctx,
                f"Variable '{nombre}' no ha sido declarada"
            )
            return None

        tipo_valor = self.visit(ctx.expresion(0))
        return tipo_declarado

    def visitExpresionSi(self, ctx):
        tipo_cond = self.visit(ctx.expresion())
        if tipo_cond and tipo_cond != "bool":
            self.registrar_error(ctx, f"Condición del if debe ser booleana, recibe {tipo_cond}")
        self.visit(ctx.bloque(0))
        if ctx.SINO():
            self.visit(ctx.bloque(1))
        return None

    def visitCicloWhile(self, ctx):
        tipo_cond = self.visit(ctx.expresion())
        if tipo_cond and tipo_cond != "bool":
            self.registrar_error(ctx, f"Condición del while debe ser booleana, recibe {tipo_cond}")

        self.en_ciclo += 1
        self.push_scope()
        self.visit(ctx.bloque())
        self.pop_scope()
        self.en_ciclo -= 1
        return None

    def visitCicloFor(self, ctx):
        if ctx.declaracion():
            self.visit(ctx.declaracion())
        else:
            self.visit(ctx.asignacion(0))
        
        tipo_cond = self.visit(ctx.expresion())
        if tipo_cond and tipo_cond != "bool":
            self.registrar_error(ctx, f"Condición del for debe ser booleana, recibe {tipo_cond}")
        
        self.visit(ctx.asignacion()[-1])

        self.en_ciclo += 1
        self.push_scope()
        self.visit(ctx.bloque())
        self.pop_scope()
        self.en_ciclo -= 1
        return None
    
    def visitSwitchStmt(self, ctx):
        # validar expresión de control
        self.visit(ctx.expresion())

        self.en_ciclo += 1

        self.push_scope()

        for case_ctx in ctx.caseStmt():
            for s in case_ctx.sentencia():
                self.visit(s)

        if ctx.defaultStmt():
            for s in ctx.defaultStmt().sentencia():
                self.visit(s)

        self.pop_scope()

        self.en_ciclo -= 1

        return None
    
    def visitBreakStmt(self, ctx):
        if self.en_ciclo == 0:
            self.registrar_error(ctx, "break fuera de un ciclo")
        return None

    def visitContinueStmt(self, ctx):
        if self.en_ciclo == 0:
            self.registrar_error(ctx, "continue fuera de un ciclo")
        return None
    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        tipo = self.get_tipo_var(nombre)
        if not tipo:
            self.registrar_error(ctx, f"Función '{nombre}' no definida")
            return "int"
        return tipo

    def visitReturnStmt(self, ctx):
        if ctx.expresion():
            return self.visit(ctx.expresion())
        return "void"

    
    def visitPrintt(self, ctx):
        self.visit(ctx.expresion())
        return None

    def visitExpresion(self, ctx):
        tipo_cond = self.visit(ctx.comparacion())
        # ternario
        if ctx.getChildCount() > 1:
            tipo_true = self.visit(ctx.expresion(0))
            tipo_false = self.visit(ctx.expresion(1))
            if tipo_true != tipo_false:
                self.registrar_error(
                    ctx,
                    f"Ternario incompatible: {tipo_true} y {tipo_false}"
                )
            return tipo_true
        return tipo_cond
    
    def visitComparacion(self, ctx):
        # Si hay operadores relacionales, retorna bool
        if len(ctx.suma()) > 1:
            for i in range(len(ctx.suma())):
                self.visit(ctx.suma(i))
            return "bool"
        # Si es solo una expresión, retorna su tipo
        return self.visit(ctx.suma(0))
    
    def visitSuma(self, ctx):
        resultado = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            t_sig = self.visit(ctx.termino(i))
            if resultado == "string" or t_sig == "string":
                resultado = "string"
            elif resultado == "float" or t_sig == "float":
                resultado = "float"
            else:
                resultado = "int"
        return resultado
    
    def visitTermino(self, ctx):
        resultado = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            t_sig = self.visit(ctx.factor(i))

            # detectar operador
            op = ctx.getChild(2*i - 1).getText()

            if op == '%':
                if resultado != "int" or t_sig != "int":
                    self.registrar_error(ctx, "Operador % solo válido para enteros")
                resultado = "int"
            else:
                if resultado == "float" or t_sig == "float":
                    resultado = "float"
                else:
                    resultado = "int"

        return resultado
    
    def visitFactor(self, ctx):
        if ctx.NUM():
            return "int"

        if ctx.STRING():
            return "string"

        # acceso array
        if ctx.ID() and ctx.CORI():
            nombre = ctx.ID(0).getText()
            tipo = self.get_tipo_var(nombre)

            if not tipo:
                self.registrar_error(ctx, f"Variable '{nombre}' no está definida")
                return "int"

            if not tipo.endswith("[]"):
                self.registrar_error(ctx, f"'{nombre}' no es un arreglo")
                return "int"

            tipo_index = self.visit(ctx.expresion())
            if tipo_index != "int":
                self.registrar_error(ctx, f"Índice de arreglo debe ser int")

            return tipo.replace("[]", "")
        #acceso structs
        if len(ctx.ID()) == 2:
            nombre_struct = ctx.ID(0).getText()
            campo = ctx.ID(1).getText()

            tipo_struct = self.get_tipo_var(nombre_struct)

            if not tipo_struct:
                self.registrar_error(
                    ctx,
                    f"Variable '{nombre_struct}' no está definida"
                )
                return "int"

            return "int"

        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())

        if ctx.expresion():
            return self.visit(ctx.expresion())
        
        if ctx.TIPO():
            tipo_destino = ctx.TIPO().getText()

            self.visit(ctx.factor())

            return tipo_destino

        if ctx.NOT():
            return "bool"
        
        if ctx.RES():
            return self.visit(ctx.factor())

        return "void"