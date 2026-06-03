import time
import sys
from antlr4 import *
from custom_errors import ErrorHandler
from lexer_phase import LexerPhase
from parser_phase import ParserPhase
from tac_generator import TACGenerator
from visitor import Visitor
from semantic_phase import SemanticPhase
from ir_generator import IRGenerator 
from optimizer import Optimizer
import os
import shutil
import subprocess


class Pipeline:
    def __init__(self):
        self.error_handler = ErrorHandler(detener_en_primera_falla=True)
        self.ast = None
        self.resultados = {}
    
    def ejecutar(self, codigo):
        self.error_handler.limpiar()
        self.resultados = {}
        
        print("\n" + "="*60)
        print("COMPILADOR - PIPELINE")
        print("="*60)
        
        if not self._fase_lexica(codigo):
            return self._resumen()
        
        if not self._fase_sintactica(codigo):
            return self._resumen()
        
        if not self._fase_semantica():
            return self._resumen()
        
        if not self._fase_tac():
            return self._resumen()
        
        if not self._fase_llvm():
            return self._resumen()
        
        self._fase_ejecucion()

        if not self._fase_optimizacion_o3():
            return self._resumen()
        
        self._fase_binarios()
        
        return self._resumen()
    
    def _fase_lexica(self, codigo):
        print("\n[FASE 1] Análisis Léxico")
        print("-" * 40)
        inicio = time.time()
        
        fase = LexerPhase(self.error_handler)
        exitoso, tokens = fase.ejecutar(codigo)
        tiempo = (time.time() - inicio) * 1000
        
        self.resultados["lexico"] = {"exitoso": exitoso, "tiempo_ms": tiempo}
        print(f"  {'Nice :D' if exitoso else 'Error :/'} {tiempo:.2f} ms - {len(tokens)} tokens")
        return exitoso
    
    def _fase_sintactica(self, codigo):
        print("\n[FASE 2] Análisis Sintáctico")
        print("-" * 40)
        inicio = time.time()
        
        fase = ParserPhase(self.error_handler)
        exitoso, self.ast = fase.ejecutar(codigo)
        tiempo = (time.time() - inicio) * 1000
        
        self.resultados["sintactico"] = {"exitoso": exitoso, "tiempo_ms": tiempo}
        print(f"  {'Nice :D' if exitoso else 'Error :/'} {tiempo:.2f} ms - AST generado")
        return exitoso

    def _fase_semantica(self):
        print("\n[FASE 3] Análisis Semántico")
        print("-" * 40)
        inicio = time.time()
        
        try:
            fase = SemanticPhase(self.error_handler)
            exitoso, _ = fase.ejecutar(self.ast)
            tiempo = (time.time() - inicio) * 1000
            
            self.resultados["semantico"] = {"exitoso": exitoso, "tiempo_ms": tiempo}
            print(f"  {'Nice :D' if exitoso else 'Error :/'} {tiempo:.2f} ms")
            
            return exitoso
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            self.resultados["semantico"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f"  Error: {e}")
            return False
    
    def _fase_tac(self):
        print("\n[FASE 4] Generación TAC")
        print("-" * 40)
        inicio = time.time()
        
        try:
            tac_gen = TACGenerator()
            codigo_tac = tac_gen.visit(self.ast)
            tiempo = (time.time() - inicio) * 1000
            
            with open("salida.tac", "w", encoding='utf-8') as f:
                f.write(codigo_tac)
            
            self.resultados["tac"] = {"exitoso": True, "tiempo_ms": tiempo}
            print(f"  Nice {tiempo:.2f} ms - {len(tac_gen.instructions)} instrucciones")
            print(f"  Archivo: salida.tac")
            return True
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            self.resultados["tac"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f"  Error: {e}")
            return False

    def _fase_llvm(self):
        print("\n[FASE 5] Generación LLVM IR")
        print("-" * 40)
        inicio = time.time()
        try:
            generator = IRGenerator()
            codigo_llvm = generator.visit(self.ast)
            tiempo = (time.time() - inicio) * 1000
            
            with open("salida.ll", "w", encoding='utf-8') as f:
                f.write(codigo_llvm)
                
            self.resultados["llvm"] = {"exitoso": True, "tiempo_ms": tiempo}
            print(f"  Nice :D {tiempo:.2f} ms - Archivo: salida.ll")
            return True
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            self.resultados["llvm"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f"  Error: {e}")
            return False
        

    def _fase_ejecucion(self):
        print("\n[FASE 6] Ejecución (Interpreter Mode)")
        print("-" * 40)
        inicio = time.time()
        
        try:
            visitor = Visitor()
            visitor.visit(self.ast)
            tiempo = (time.time() - inicio) * 1000
            
            self.resultados["ejecucion"] = {"exitoso": True, "tiempo_ms": tiempo}
            print(f"  Nice {tiempo:.2f} ms - Ejecución completada")
            return True
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            self.resultados["ejecucion"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f"  Error: {e}")
            return False
    
    def _fase_optimizacion_o3(self):
        print("\n[FASE 7] Optimización LLVM O3")
        print("-" * 40)
        inicio = time.time()

        try:
            with open("salida.ll", "r", encoding="utf-8") as f:
                ir_original = f.read()

            optimizer = Optimizer()
            ir_optimizado, metricas = optimizer.optimizar_o3(ir_original)

            with open("salida.opt.ll", "w", encoding="utf-8") as f:
                f.write(ir_optimizado)

            tiempo = (time.time() - inicio) * 1000

            self.resultados["optimizacion_o3"] = {
                "exitoso": True,
                "tiempo_ms": tiempo,
                "metricas": metricas
            }

            print(f"  Nice :D {tiempo:.2f} ms - Archivo: salida.opt.ll")
            print("  Métricas O3:")
            print(f"    Instrucciones antes   : {metricas['instrucciones_antes']}")
            print(f"    Instrucciones después : {metricas['instrucciones_despues']}")
            print(f"    Reducción             : {metricas['reduccion_porcentaje']}%")

            return True

        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            self.resultados["optimizacion_o3"] = {
                "exitoso": False,
                "tiempo_ms": (time.time() - inicio) * 1000
            }
            print(f"  Error: {e}")
            return False
        
    def _fase_binarios(self):
        print("\n[FASE 8] Generación de Binarios Nativos")
        print("-" * 40)

        inicio = time.time()

        for archivo in ["programa_linux", "programa.exe", "programa.obj"]:
            if os.path.exists(archivo):
                os.remove(archivo)
                resultado = {
                    "exitoso": True,
                    "tiempo_ms": 0,
                    "linux": None,
                    "windows": None,
                    "errores": []
                }

        ir_file = "salida.ll"

        if not os.path.exists(ir_file):
            ir_file = "salida.ll"

        try:
            # ==========================
            # BINARIO LINUX
            # ==========================
            if shutil.which("clang"):
                linux_bin = "programa_linux"

                cmd_linux = [
                    "clang",
                    ir_file,
                    "-o",
                    linux_bin
                ]

                proc_linux = subprocess.run(
                    cmd_linux,
                    capture_output=True,
                    text=True
                )

                if proc_linux.returncode == 0:
                    resultado["linux"] = linux_bin
                    print(f"  Linux   : Nice :D {linux_bin}")
                else:
                    resultado["exitoso"] = False
                    resultado["errores"].append(proc_linux.stderr)
                    print("  Linux   : Error :/")
                    print(proc_linux.stderr)
            else:
                resultado["exitoso"] = False
                resultado["errores"].append("clang no está instalado")
                print("  Linux   : clang no encontrado")

            # ==========================
            # BINARIO WINDOWS
            # ==========================
            if shutil.which("llc") and shutil.which("x86_64-w64-mingw32-gcc"):
                obj_file = "programa.obj"
                exe_file = "programa.exe"

                cmd_obj = [
                    "llc",
                    "-mtriple=x86_64-w64-windows-gnu",
                    "-filetype=obj",
                    ir_file,
                    "-o",
                    obj_file
                ]

                proc_obj = subprocess.run(
                    cmd_obj,
                    capture_output=True,
                    text=True
                )

                if proc_obj.returncode != 0:
                    resultado["exitoso"] = False
                    resultado["errores"].append(proc_obj.stderr)
                    print("  Windows : Error generando .obj")
                    print(proc_obj.stderr)
                else:
                    cmd_exe = [
                        "x86_64-w64-mingw32-gcc",
                        obj_file,
                        "-o",
                        exe_file
                    ]

                    proc_exe = subprocess.run(
                        cmd_exe,
                        capture_output=True,
                        text=True
                    )

                    if proc_exe.returncode == 0:
                        resultado["windows"] = exe_file
                        print(f"  Windows : Nice :D {exe_file}")
                        destino_win = "/mnt/c/Users/motit/Desktop/programa_compilador.exe"
                        try:
                            shutil.copyfile(exe_file, destino_win)
                            print(f"  Copiado : {destino_win}")
                        except Exception as e:
                            print(f"  Aviso   : no se pudo copiar a Windows: {e}")
                    else:
                        resultado["exitoso"] = False
                        resultado["errores"].append(proc_exe.stderr)
                        print("  Windows : Error generando .exe")
                        print(proc_exe.stderr)
            else:
                print("  Windows : omitido, falta llc o x86_64-w64-mingw32-gcc")

        except Exception as e:
            resultado["exitoso"] = False
            resultado["errores"].append(str(e))
            print(f"  Error: {e}")

        tiempo = (time.time() - inicio) * 1000
        resultado["tiempo_ms"] = tiempo

        self.resultados["binarios"] = resultado

        print(f"  Tiempo  : {tiempo:.2f} ms")

        return resultado["exitoso"]

    def _resumen(self):
        print("\n" + "="*60)
        print("RESUMEN")
        print("="*60)
        
        for nombre, r in self.resultados.items():
            status = "Nice :D" if r["exitoso"] else "Error :/"
            print(f"  {status} {nombre.capitalize():12} : {r['tiempo_ms']:8.2f} ms")
        
        total = sum(r["tiempo_ms"] for r in self.resultados.values())
        print(f"\n  TOTAL: {total:.2f} ms")
        
        if self.error_handler.tiene_errores():
            print(f"\n  ERRORES: {len(self.error_handler.errores)}")
            for e in self.error_handler.errores[:3]:
                print(f"     • {e}")
        
        print("="*60)
        return all(r["exitoso"] for r in self.resultados.values())


def main():
    archivo = sys.argv[1] if len(sys.argv) > 1 else "prueba.txt"
    print(f"\nArchivo: {archivo}")
    
    with open(archivo, 'r', encoding='utf-8') as f:
        codigo = f.read()
    
    pipeline = Pipeline()
    ok = pipeline.ejecutar(codigo)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()