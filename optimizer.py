import llvmlite.binding as llvm


class Optimizer:
    def __init__(self):
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

    def contar_instrucciones(self, ir_code):
        ignorar = (";", "target", "source_filename", "declare", "define", "{", "}", "entry:")
        count = 0

        for linea in ir_code.splitlines():
            limpia = linea.strip()
            if not limpia:
                continue
            if limpia.startswith(ignorar):
                continue
            if limpia.endswith(":"):
                continue
            count += 1

        return count

    def optimizar_o3(self, ir_code):
        modulo = llvm.parse_assembly(ir_code)
        modulo.verify()

        antes = self.contar_instrucciones(str(modulo))

        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()

        pto = llvm.create_pipeline_tuning_options(speed_level=3, size_level=0)
        pto.loop_vectorization = True
        pto.slp_vectorization = True
        pto.loop_unrolling = True

        pass_builder = llvm.create_pass_builder(target_machine, pto)
        mpm = pass_builder.getModulePassManager()

        mpm.run(modulo, pass_builder)

        ir_optimizado = str(modulo)
        despues = self.contar_instrucciones(ir_optimizado)

        reduccion = 0
        if antes > 0:
            reduccion = ((antes - despues) / antes) * 100

        metricas = {
            "instrucciones_antes": antes,
            "instrucciones_despues": despues,
            "reduccion_porcentaje": round(reduccion, 2)
        }

        return ir_optimizado, metricas