import time
import sys
from antlr4 import *
from custom_errors import ErrorHandler
from lexer_phase import LexerPhase
from parser_phase import ParserPhase
from semantic_phase import SemanticPhase
from interpreter_phase import InterpreterPhase
from tac_generator import TACGenerator
from ir_generator import IRGenerator



class Pipeline:
    def __init__(self):
        self.error_handler = ErrorHandler(detener_en_primera_falla=True)
        self.ast = None
        self.symbol_table = None
        self.resultados = {}
    
    def ejecutar(self, codigo):
        self.error_handler.limpiar()
        self.resultados = {}
        
        print("\n" + "="*60)
        print("COMPILADOR - PIPELINE v3.0")
        print("="*60)
        
        # Fase 1: Léxico
        if not self._fase_lexica(codigo):
            return self._resumen()
        
        # Fase 2: Sintáctico
        if not self._fase_sintactica(codigo):
            return self._resumen()
        
        # Fase 3: Semántico
        if not self._fase_semantica():
            return self._resumen()
        
        # Fase 4: Generación TAC
        if not self._fase_tac():
            return self._resumen()
        
        # Fase 5: LLVM IR
        if not self._fase_ir():
            return self._resumen()
        # Fase 6
        self._fase_ejecucion()
        
        return self._resumen()
    
    def _fase_lexica(self, codigo):
        print("\n[FASE 1] Análisis Léxico")
        print("-" * 40)
        inicio = time.time()
        
        fase = LexerPhase(self.error_handler)
        exitoso, tokens = fase.ejecutar(codigo)
        tiempo = (time.time() - inicio) * 1000
        
        self.resultados["lexico"] = {"exitoso": exitoso, "tiempo_ms": tiempo}
        print(f"  {'Nicee' if exitoso else 'Erroor'} {tiempo:.2f} ms - {len(tokens)} tokens")
        return exitoso
    
    def _fase_sintactica(self, codigo):
        print("\n[FASE 2] Análisis Sintáctico")
        print("-" * 40)
        inicio = time.time()
        
        fase = ParserPhase(self.error_handler)
        exitoso, self.ast = fase.ejecutar(codigo)
        tiempo = (time.time() - inicio) * 1000
        
        self.resultados["sintactico"] = {"exitoso": exitoso, "tiempo_ms": tiempo}
        print(f"  {'Nicee' if exitoso else 'Errooor'} {tiempo:.2f} ms - AST generado")
        return exitoso
    
    def _fase_semantica(self):
        print("\n[FASE 3] Análisis Semántico")
        print("-" * 40)
        inicio = time.time()
        
        fase = SemanticPhase(self.error_handler)
        exitoso, self.symbol_table = fase.ejecutar(self.ast)
        tiempo = (time.time() - inicio) * 1000
        
        self.resultados["semantico"] = {"exitoso": exitoso, "tiempo_ms": tiempo}
        print(f"  {'Nicee' if exitoso else 'Erroor'} {tiempo:.2f} ms - Tabla de símbolos")
        return exitoso
    
    def _fase_tac(self):
        print("\n[FASE 4] Generación TAC (Código de Tres Direcciones)")
        print("-" * 40)
        inicio = time.time()
        
        try:
            tac_gen = TACGenerator()
            codigo_tac = tac_gen.visit(self.ast)
            tiempo = (time.time() - inicio) * 1000
            
            # Guardar en archivo
            with open("salida.tac", "w", encoding='utf-8') as f:
                f.write(codigo_tac)
            
            self.resultados["tac"] = {"exitoso": True, "tiempo_ms": tiempo}
            print(f" Niicee! {tiempo:.2f} ms - {len(tac_gen.instructions)} instrucciones TAC")
            print(f"Archivo generado: salida.tac")
            
            # Mostrar primeras líneas del TAC
            lineas = codigo_tac.split('\n')
            print(f"\n  --- Primeras líneas del TAC ---")
            for linea in lineas[:10]:
                print(f"    {linea}")
            if len(lineas) > 10:
                print(f"    ... y {len(lineas)-10} líneas más")
            
            return True
            
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, f"Error generando TAC: {str(e)}")
            self.resultados["tac"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f"Error: {e}")
            return False
        
    
    def _fase_ir(self):
        print("\n[FASE 5] Generación LLVM IR")
        print("-" * 40)
        inicio = time.time()
        
        try:
            ir_gen = IRGenerator()
            codigo_ir = ir_gen.visit(self.ast)
            tiempo = (time.time() - inicio) * 1000
            
            # Guardar archivo .ll
            with open("salida.ll", "w", encoding='utf-8') as f:
                f.write(codigo_ir)
            
            self.resultados["ir"] = {"exitoso": True, "tiempo_ms": tiempo}
            print(f" Niicee! {tiempo:.2f} ms - {len(codigo_ir.split(chr(10)))} líneas")
            print(f"Archivo generado: salida.ll")
            
            return True
            
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, f"Error generando IR: {str(e)}")
            self.resultados["ir"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f" Error: {e}")
            return False

    def _fase_ejecucion(self):
        print("\n[FASE 6] Ejecución")
        print("-" * 40)
        inicio = time.time()
        
        fase = InterpreterPhase(self.error_handler)
        exitoso, resultado = fase.ejecutar(self.ast)
        tiempo = (time.time() - inicio) * 1000
        
        self.resultados["ejecucion"] = {"exitoso": exitoso, "tiempo_ms": tiempo}
        print(f"  {'Niicee' if exitoso else 'Errooor'} {tiempo:.2f} ms")
        return exitoso
    
    def _resumen(self):
        print("\n" + "="*60)
        print("RESUMEN")
        print("="*60)
        
        for nombre, r in self.resultados.items():
            print(f"  {'Nicee' if r['exitoso'] else 'Errooor'} {nombre.capitalize():12} : {r['tiempo_ms']:8.2f} ms")
        
        total = sum(r["tiempo_ms"] for r in self.resultados.values())
        print(f"\nTOTAL: {total:.2f} ms")
        
        if self.error_handler.tiene_errores():
            print(f"\nERRORES: {len(self.error_handler.errores)}")
            for e in self.error_handler.errores[:3]:
                print(f"     • {e}")
        
        print("="*60)
        return all(r["exitoso"] for r in self.resultados.values())


def main():
    archivo = sys.argv[1] if len(sys.argv) > 1 else "entrada.txt"
    
    with open(archivo, 'r', encoding='utf-8') as f:
        codigo = f.read()
    
    pipeline = Pipeline()
    ok = pipeline.ejecutar(codigo)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()