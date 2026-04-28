import time
import sys
from antlr4 import *
from custom_errors import ErrorHandler
from lexer_phase import LexerPhase
from parser_phase import ParserPhase
from semantic_phase import SemanticPhase
from interpreter_phase import InterpreterPhase


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
        
        # Fase 4: Ejecución
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
    
    def _fase_ejecucion(self):
        print("\n[FASE 4] Ejecución")
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