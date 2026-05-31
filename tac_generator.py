from gramatica_finalVisitor import gramatica_finalVisitor

class TACGenerator(gramatica_finalVisitor):
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
        self.loop_stack = []
        self.switch_stack = []
        self.current_function = None
    
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"
    
    def add(self, instruction):
        self.instructions.append(instruction)
        return instruction
    
    def get_code(self):
        return "\n".join(self.instructions)
    
    # FASE INICIAL: Corregido para usar 'programa'
    def visitRoot(self, ctx):
        self.add("# Código TAC generado")
        if ctx.programa():
            for p in ctx.programa():
                self.visit(p)
        return self.get_code()

    # NAVEGACIÓN DE REGLAS
    def visitPrograma(self, ctx): 
        return self.visitChildren(ctx)
    def visitSentenciaGlobal(self, ctx): 
        return self.visitChildren(ctx)

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()

        args = []
        if ctx.argumentos():
            args = [self.visit(e) for e in ctx.argumentos().expresion()]

        temp = self.new_temp()
        self.add(f"  {temp} = call {nombre}, {', '.join(args)}")
        return temp
    def visitBloque(self, ctx):
        if ctx.sentencia():
            for s in ctx.sentencia():
                self.visit(s)

    def visitExpresion(self, ctx):
        condicion = self.visit(ctx.comparacion())
        # ternario
        if ctx.getChildCount() > 1:
            verdadero = ctx.expresion(0)
            falso = ctx.expresion(1)

            temp = self.new_temp()

            l_true = self.new_label()
            l_false = self.new_label()
            l_end = self.new_label()

            self.add(f"  if {condicion} goto {l_true}")
            self.add(f"  goto {l_false}")

            self.add(f"{l_true}:")
            val_true = self.visit(verdadero)
            self.add(f"  {temp} = {val_true}")
            self.add(f"  goto {l_end}")

            self.add(f"{l_false}:")
            val_false = self.visit(falso)
            self.add(f"  {temp} = {val_false}")

            self.add(f"{l_end}:")
            return temp

        return condicion

    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.suma(i))
            temp = self.new_temp()
            self.add(f"  {temp} = {resultado} {op} {derecha}")
            resultado = temp
        return resultado

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.termino(i))
            temp = self.new_temp()
            self.add(f"  {temp} = {resultado} {op} {derecha}")
            resultado = temp
        return resultado

    def visitTermino(self, ctx):
        resultado = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i-1).getText()
            derecha = self.visit(ctx.factor(i))
            temp = self.new_temp()
            self.add(f"  {temp} = {resultado} {op} {derecha}")
            resultado = temp
        return resultado

    def visitFactor(self, ctx):
        if ctx.RES():
            val = self.visit(ctx.getChild(1))

            temp = self.new_temp()
            self.add(f"  {temp} = -{val}")
            return temp
        
        if ctx.NUM():
            return ctx.NUM().getText()

        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.ID().getText()
            index = self.visit(ctx.expresion())

            temp = self.new_temp()
            self.add(f"  {temp} = {nombre}[{index}]")
            return temp

        if ctx.ID():
            return ctx.ID().getText()
        
        if ctx.TIPO():
            tipo_destino = ctx.TIPO().getText()
            valor = self.visit(ctx.factor())
            temp = self.new_temp()
            self.add(f"  {temp} = cast_{tipo_destino} {valor}")

            return temp

        if ctx.PAI():
            return self.visit(ctx.expresion())

        return "0"

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()

        if ctx.arrayLiteral():
            valores = [self.visit(e) for e in ctx.arrayLiteral().expresion()]
            self.add(f"{nombre} = [{', '.join(valores)}]")
            return nombre

        valor = self.visit(ctx.expresion()) if ctx.expresion() else "0"
        self.add(f"{nombre} = {valor}")
        return nombre

    def visitAsignacion(self, ctx):
        # nums[i] = valor
        if ctx.CORI():
            nombre = ctx.ID().getText()
            indice = self.visit(ctx.expresion(0))
            valor = self.visit(ctx.expresion(1))
            self.add(f"{nombre}[{indice}] = {valor}")
            return valor

        # normal
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion(0))
        self.add(f"{nombre} = {valor}")
        return valor

    def visitPrintt(self, ctx):
        valor = self.visit(ctx.expresion())
        self.add(f"  print {valor}")

    def visitExpresionSi(self, ctx):
        cond = self.visit(ctx.expresion())

        ltrue = self.new_label()
        lfalse = self.new_label()
        lend = self.new_label()

        self.add(f"  if {cond} goto {ltrue}")
        self.add(f"  goto {lfalse}")

        self.add(f"{ltrue}:")
        self.visit(ctx.bloque(0))
        self.add(f"  goto {lend}")

        self.add(f"{lfalse}:")
        if ctx.SINO():
            self.visit(ctx.bloque(1))

        self.add(f"{lend}:")

    def visitCicloWhile(self, ctx):
        L_start = self.new_label()
        L_body = self.new_label()
        L_end = self.new_label()

        self.loop_stack.append((L_start, L_end))

        self.add(f"{L_start}:")
        cond = self.visit(ctx.expresion())
        self.add(f"  if {cond} goto {L_body}")
        self.add(f"  goto {L_end}")

        self.add(f"{L_body}:")
        self.visit(ctx.bloque())

        self.add(f"  goto {L_start}")

        self.add(f"{L_end}:")
        self.loop_stack.pop()

    def visitCicloFor(self, ctx):
        # init
        if ctx.declaracion():
            self.visit(ctx.declaracion())
        else:
            self.visit(ctx.asignacion(0))

        L_start = self.new_label()
        L_body = self.new_label()
        L_end = self.new_label()

        self.loop_stack.append((L_start, L_end))

        self.add(f"{L_start}:")
        cond = self.visit(ctx.expresion())
        self.add(f"  if {cond} goto {L_body}")
        self.add(f"  goto {L_end}")

        self.add(f"{L_body}:")
        self.visit(ctx.bloque())

        # update
        self.visit(ctx.asignacion()[-1])

        self.add(f"  goto {L_start}")
        self.add(f"{L_end}:")
        self.loop_stack.pop()

    def visitSwitchStmt(self, ctx):
        valor = self.visit(ctx.expresion())
        L_end = self.new_label()
        self.switch_stack.append(L_end)
        case_labels = []

        for _ in ctx.caseStmt():
            case_labels.append(self.new_label())
        default_label = self.new_label() if ctx.defaultStmt() else L_end

        for i, case_ctx in enumerate(ctx.caseStmt()):

            valor_case = case_ctx.NUM().getText()

            temp = self.new_temp()
            self.add(f"  {temp} = {valor} == {valor_case}")
            self.add(f"  if {temp} goto {case_labels[i]}")

        self.add(f"  goto {default_label}")

        for i, case_ctx in enumerate(ctx.caseStmt()):
            self.add(f"{case_labels[i]}:")
            for s in case_ctx.sentencia():
                self.visit(s)
        # default
        if ctx.defaultStmt():
            self.add(f"{default_label}:")
            for s in ctx.defaultStmt().sentencia():
                self.visit(s)
        self.add(f"{L_end}:")
        self.switch_stack.pop()

    def visitBreakStmt(self, ctx):
        if self.switch_stack:
            self.add(f"  goto {self.switch_stack[-1]}")
            return

        if self.loop_stack:
            _, L_end = self.loop_stack[-1]
            self.add(f"  goto {L_end}")

    def visitContinueStmt(self, ctx):
        if self.loop_stack:
            L_start, _ = self.loop_stack[-1]
            self.add(f"  goto {L_start}")

    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()
        self.current_function = nombre
        self.add(f"\nfunc {nombre}:")
        self.visit(ctx.bloque())
        self.add(f"endfunc {nombre}\n")
        self.current_function = None

    def visitReturnStmt(self, ctx):
        valor = self.visit(ctx.expresion()) if ctx.expresion() else ""
        self.add(f"  return {valor}")
        return valor