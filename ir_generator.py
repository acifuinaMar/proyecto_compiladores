from llvmlite import ir
from gramatica_finalVisitor import gramatica_finalVisitor

class IRGenerator(gramatica_finalVisitor):
    def __init__(self):
        self.module = ir.Module(name="compilador_umg")
        self.builder = None
        self.func = None
        self.variables = {}
        self.int_type = ir.IntType(32)

    def visitRoot(self, ctx):
        func_type = ir.FunctionType(self.int_type, [])
        self.func = ir.Function(self.module, func_type, name="main")
        block = self.func.append_basic_block("entry")
        self.builder = ir.IRBuilder(block)

        if ctx.programa():
            for p in ctx.programa():
                self.visit(p)

        # Retorno de seguridad para lli
        if 'suma' in self.variables:
            self.builder.ret(self.builder.load(self.variables['suma']))
        else:
            self.builder.ret(ir.Constant(self.int_type, 0))
        
        return str(self.module)

    def visitExpresion(self, ctx):
        # CORRECCIÓN: Saltar a comparacion() para evitar el error de atributo
        return self.visit(ctx.comparacion())

    def visitComparacion(self, ctx):
        left = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            op = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.suma(i))
            if op == '<=': left = self.builder.icmp_signed('<=', left, right)
            elif op == '>=': left = self.builder.icmp_signed('>=', left, right)
            elif op == '<': left = self.builder.icmp_signed('<', left, right)
            elif op == '>': left = self.builder.icmp_signed('>', left, right)
            elif op == '==': left = self.builder.icmp_signed('==', left, right)
            elif op == '!=': left = self.builder.icmp_signed('!=', left, right)
        return left

    def visitSuma(self, ctx):
        res = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i-1).getText()
            val = self.visit(ctx.termino(i))
            res = self.builder.add(res, val) if op == '+' else self.builder.sub(res, val)
        return res

    def visitTermino(self, ctx):
        res = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i-1).getText()
            val = self.visit(ctx.factor(i))
            res = self.builder.mul(res, val) if op == '*' else self.builder.sdiv(res, val)
        return res

    def visitFactor(self, ctx):
        if ctx.NUM(): return ir.Constant(self.int_type, int(ctx.NUM().getText()))
        if ctx.ID(): return self.builder.load(self.variables[ctx.ID().getText()])
        if ctx.PAI(): return self.visit(ctx.expresion())
        return ir.Constant(self.int_type, 0)

    def visitDeclaracion(self, ctx):
        name = ctx.ID().getText()
        ptr = self.builder.alloca(self.int_type, name=name)
        self.variables[name] = ptr
        if ctx.expresion():
            self.builder.store(self.visit(ctx.expresion()), ptr)

    def visitAsignacion(self, ctx):
        name = ctx.ID().getText()
        val = self.visit(ctx.expresion())
        if name in self.variables:
            self.builder.store(val, self.variables[name])
        return val

    def visitCicloFor(self, ctx):
        self.visit(ctx.getChild(2)) # Init
        cond_b = self.func.append_basic_block("f_cond")
        body_b = self.func.append_basic_block("f_body")
        step_b = self.func.append_basic_block("f_step")
        end_b = self.func.append_basic_block("f_end")

        self.builder.branch(cond_b)
        self.builder.position_at_start(cond_b)
        cond_val = self.visit(ctx.expresion())
        if cond_val.type == self.int_type:
            cond_val = self.builder.icmp_signed('!=', cond_val, ir.Constant(self.int_type, 0))
        self.builder.cbranch(cond_val, body_b, end_b)

        self.builder.position_at_start(body_b)
        self.visit(ctx.bloque())
        self.builder.branch(step_b)

        self.builder.position_at_start(step_b)
        self.visit(ctx.asignacion())
        self.builder.branch(cond_b)
        self.builder.position_at_start(end_b)

    def visitBloque(self, ctx):
        if ctx.sentencia():
            for s in ctx.sentencia(): self.visit(s)

    def visitPrograma(self, ctx): return self.visitChildren(ctx)
    def visitSentenciaGlobal(self, ctx): return self.visitChildren(ctx)
    def visitPrintt(self, ctx): return self.visit(ctx.expresion())