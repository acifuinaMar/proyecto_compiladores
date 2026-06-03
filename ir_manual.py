import difflib
import llvmlite.binding as llvm


class IRManual:
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

    def generar_diff(self, ir_antes, ir_despues):
        diff = difflib.unified_diff(
            ir_antes.splitlines(),
            ir_despues.splitlines(),
            fromfile="IR original",
            tofile="IR manual optimizado",
            lineterm=""
        )
        return "\n".join(diff)

    def aplicar_passes(self, ir_code, passes):
        modulo = llvm.parse_assembly(ir_code)
        modulo.verify()

        antes = self.contar_instrucciones(str(modulo))

        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()

        pto = llvm.create_pipeline_tuning_options(speed_level=0, size_level=0)
        pass_builder = llvm.create_pass_builder(target_machine, pto)

        mpm = llvm.create_new_module_pass_manager()

        passes_aplicados = []

        mapa_passes = {
            "instcombine": ["add_instruction_combine_pass"],
            "simplifycfg": ["add_simplify_cfg_pass"],
            "dce": ["add_dead_code_elimination_pass"],
            "global-dce": ["add_global_dead_code_eliminate_pass"],
            "aggressive-dce": ["add_aggressive_dce_pass"],
            "inline": ["add_always_inliner_pass", "add_partial_inliner_pass"],
            "loop-unroll": ["add_loop_unroll_pass"],
            "mem2reg": ["add_sroa_pass"],
        }

        passes_aplicados = []

        for p in passes:
            if p not in mapa_passes:
                raise Exception(f"Pass no soportado: {p}")

            agregado = False

            for metodo in mapa_passes[p]:
                if hasattr(mpm, metodo):
                    getattr(mpm, metodo)()
                    passes_aplicados.append(p)
                    agregado = True
                    break

            if not agregado:
                disponibles = [m for m in dir(mpm) if m.startswith("add_")]
                raise Exception(
                    f"El pass '{p}' no está disponible en esta versión de llvmlite. "
                    f"Métodos disponibles: {disponibles}"
                )

        mpm.run(modulo, pass_builder)

        ir_despues = str(modulo)
        despues = self.contar_instrucciones(ir_despues)

        reduccion = 0
        if antes > 0:
            reduccion = ((antes - despues) / antes) * 100

        metricas = {
            "passes_aplicados": passes_aplicados,
            "instrucciones_antes": antes,
            "instrucciones_despues": despues,
            "reduccion_porcentaje": round(reduccion, 2),
        }

        diff = self.generar_diff(ir_code, ir_despues)

        return ir_despues, metricas, diff
