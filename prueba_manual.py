from ir_manual import IRManual

with open("salida.ll", "r", encoding="utf-8") as f:
    ir = f.read()

manual = IRManual()

pruebas = [
    ["mem2reg"],
    ["instcombine"],
    ["simplifycfg"],
    ["dce"],
    ["loop-unroll"],
    ["mem2reg", "instcombine", "simplifycfg", "dce"]
]

for passes in pruebas:
    ir_opt, metricas, diff = manual.aplicar_passes(ir, passes)

    nombre = "_".join(passes).replace("-", "_")

    with open(f"salida.manual.{nombre}.ll", "w", encoding="utf-8") as f:
        f.write(ir_opt)

    with open(f"salida.manual.{nombre}.diff", "w", encoding="utf-8") as f:
        f.write(diff)

    print(passes, metricas)