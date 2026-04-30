import time
import sys
from antlr4 import *
from custom_errors import ErrorHandler
from lexer_phase import LexerPhase
from parser_phase import ParserPhase
from tac_generator import TACGenerator
from visitor import Visitor
from semantic_phase import SemanticPhase


class Pipeline:
    def __init__(self):
        self.error_handler = ErrorHandler(detener_en_primera_falla=True)
        self.ast = None
        self.resultados = {}
    
    
    def ejecutar(self, codigo):
        self.error_handler.limpiar()
        self.resultados = {}
        
        print("\n" + "="*60)
        print("COMPILADOR - PIPELINE v3.0")
        print("="*60)
        
        if not self._fase_lexica(codigo):
            return self._resumen()
        
        if not self._fase_sintactica(codigo):
            return self._resumen()
        
        if not self._fase_semantica():
            return self._resumen()
        
        if not self._fase_tac():
            return self._resumen()
        
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
            print(f" Nice{tiempo:.2f} ms - {len(tac_gen.instructions)} instrucciones")
            print(f" Archivo: salida.tac")
            
            print("\n--- Código TAC generado ---")
            print(codigo_tac)
            
            return True
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            self.resultados["tac"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f" Error: {e}")
            return False
    
    def _fase_ejecucion(self):
        print("\n[FASE 5] Ejecución")
        print("-" * 40)
        inicio = time.time()
        
        try:
            visitor = Visitor()
            visitor.visit(self.ast)
            tiempo = (time.time() - inicio) * 1000
            
            self.resultados["ejecucion"] = {"exitoso": True, "tiempo_ms": tiempo}
            print(f" Nice {tiempo:.2f} ms - Ejecución completada")
            return True
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            self.resultados["ejecucion"] = {"exitoso": False, "tiempo_ms": (time.time() - inicio) * 1000}
            print(f" Error: {e}")
            return False
    
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
            print(f"\n ERRORES: {len(self.error_handler.errores)}")
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