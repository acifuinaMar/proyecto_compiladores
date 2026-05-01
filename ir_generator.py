import llvmlite.binding as llvm
from llvmlite import ir
from gramatica_finalVisitor import gramatica_finalVisitor

class IRGenerator(gramatica_finalVisitor):
    def __init__(self):
        # Inicialización del entorno de LLVM
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        
        target_triple = llvm.get_process_triple()
        self.module = ir.Module(name="compilador_umg_final")
        self.module.triple = target_triple
        
        self.builder = None
        self.func = None
        self.variables = {}
        
        # Definición de tipos básicos
        self.int_type = ir.IntType(32)
        self.char_ptr = ir.IntType(8).as_pointer()

        # Declaración de la función printf para la salida de datos
        printf_ty = ir.FunctionType(self.int_type, [self.char_ptr], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

    def visitRoot(self, ctx):
        func_type = ir.FunctionType(self.int_type, [])
        self.func = ir.Function(self.module, func_type, name="main")
        entry_block = self.func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry_block)

        self.visitChildren(ctx)

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
        return str(self.module)

    # --- MANEJO DE VARIABLES Y ARREGLOS ---
    def visitDeclaracion(self, ctx):
        name = ctx.ID().getText()
        # Si la gramática detecta corchetes [], es un arreglo
        if ctx.CORI():  
            size = 10 
            if ctx.arrayLiteral():
                expr_list = ctx.arrayLiteral().expresion()
                size = len(expr_list)
            
            arr_type = ir.ArrayType(self.int_type, size)
            with self.builder.goto_entry_block():
                ptr = self.builder.alloca(arr_type, name=name)
            self.variables[name] = ptr

            if ctx.arrayLiteral():
                for i, expr_ctx in enumerate(expr_list):
                    val = self.visit(expr_ctx)
                    p_idx = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), 
                                                 ir.Constant(self.int_type, i)])
                    self.builder.store(val, p_idx)
        else:
            # Declaración de variable simple
            with self.builder.goto_entry_block():
                ptr = self.builder.alloca(self.int_type, name=name)
            self.variables[name] = ptr
            if ctx.expresion():
                val = self.visit(ctx.expresion())
                self.builder.store(val, ptr)

    def visitAsignacion(self, ctx):
        name = ctx.ID().getText()
        val = self.visit(ctx.expresion())
        if name in self.variables:
            self.builder.store(val, self.variables[name])
        return val

    # --- OPERACIONES ARITMÉTICAS ---
    def visitTermino(self, ctx):
        """Maneja *, / y el residuo %"""
        res = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i-1).getText()
            val = self.visit(ctx.factor(i))
            
            if op == '*':
                res = self.builder.mul(res, val)
            elif op == '/':
                res = self.builder.sdiv(res, val)
            elif op == '%':
                # CORRECCIÓN: srem para obtener el residuo correcto
                res = self.builder.srem(res, val)
        return res

    def visitSuma(self, ctx):
        """Maneja + y -"""
        res = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i-1).getText()
            val = self.visit(ctx.termino(i))
            if op == '+': 
                res = self.builder.add(res, val)
            else: 
                res = self.builder.sub(res, val)
        return res

    # --- CONTROL DE FLUJO ---
    def visitExpresionSi(self, ctx):
        cond_val = self.visit(ctx.expresion())
        if ctx.SINO():
            with self.builder.if_else(cond_val) as (then, otherwise):
                with then:
                    self.visit(ctx.bloque(0))
                with otherwise:
                    self.visit(ctx.bloque(1))
        else:
            with self.builder.if_then(cond_val):
                self.visit(ctx.bloque(0))

    def visitCicloWhile(self, ctx):
        u_id = id(ctx)
        cond_b = self.func.append_basic_block(f"w_cond_{u_id}")
        body_b = self.func.append_basic_block(f"w_body_{u_id}")
        end_b = self.func.append_basic_block(f"w_end_{u_id}")

        self.builder.branch(cond_b)
        self.builder.position_at_start(cond_b)
        cond_val = self.visit(ctx.expresion())
        self.builder.cbranch(cond_val, body_b, end_b)

        self.builder.position_at_start(body_b)
        self.visit(ctx.bloque())
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_b)
        self.builder.position_at_start(end_b)

    def visitCicloFor(self, ctx):
        u_id = id(ctx)
        cond_b = self.func.append_basic_block(f"f_cond_{u_id}")
        body_b = self.func.append_basic_block(f"f_body_{u_id}")
        inc_b = self.func.append_basic_block(f"f_inc_{u_id}")
        end_b = self.func.append_basic_block(f"f_end_{u_id}")

        # Inicialización
        self.visit(ctx.getChild(2))
        self.builder.branch(cond_b)

        # Condición
        self.builder.position_at_start(cond_b)
        cond_val = self.visit(ctx.expresion())
        self.builder.cbranch(cond_val, body_b, end_b)

        # Cuerpo
        self.builder.position_at_start(body_b)
        self.visit(ctx.bloque())
        if not self.builder.block.is_terminated:
            self.builder.branch(inc_b)

        # Incremento
        self.builder.position_at_start(inc_b)
        asignaciones = ctx.asignacion()
        idx_inc = 1 if len(asignaciones) > 1 else 0
        self.visit(asignaciones[idx_inc])
        self.builder.branch(cond_b)

        self.builder.position_at_start(end_b)

    # --- FACTORES Y SALIDA ---
    def visitFactor(self, ctx):
        if ctx.NUM(): 
            return ir.Constant(self.int_type, int(ctx.NUM().getText()))
        if ctx.ID(): 
            name = ctx.ID().getText()
            ptr = self.variables.get(name)
            if ptr:
                if ctx.CORI(): 
                    idx = self.visit(ctx.expresion())
                    p_idx = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), idx])
                    return self.builder.load(p_idx, name=f"arr_load_{name}")
                return self.builder.load(ptr, name=f"load_{name}")
        if ctx.PAI(): 
            return self.visit(ctx.expresion())
        return ir.Constant(self.int_type, 0)

    def visitPrintt(self, ctx):
        val = self.visit(ctx.expresion())
        fmt = "%d\n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=f"fstr_{id(ctx)}")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_ptr = self.builder.bitcast(global_fmt, self.char_ptr)
        self.builder.call(self.printf, [fmt_ptr, val])

    def visitComparacion(self, ctx):
        left = self.visit(ctx.suma(0))
        if len(ctx.suma()) > 1:
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.suma(1))
            return self.builder.icmp_signed(op, left, right)
        return left