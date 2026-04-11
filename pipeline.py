import sys
from antlr4 import *
from expresionLexer import expresionLexer
from expresionParser import expresionParser
from antlr4.error.ErrorListener import ErrorListener
from semantic_visitor import SemanticVisitor
from visitor import Visitor

# Manejador de errores para capturar fallos de sintaxis o léxicos
class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        tipo = "Sintáctico" if offendingSymbol else "Léxico"
        self.errores.append(f"[Error {tipo}] Línea {line}, Columna {column}: {msg}")

    def tiene_errores(self): 
        return len(self.errores) > 0

def run_pipeline(archivo_entrada):
    print(f"Iniciando Pipeline: {archivo_entrada}")
    try:
        # Lectura del archivo
        input_stream = FileStream(archivo_entrada, encoding='utf-8')
        
        # Análisis Léxico
        lexer = expresionLexer(input_stream)
        error_handler = CustomErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_handler)
        
        # Análisis Sintáctico
        token_stream = CommonTokenStream(lexer)
        parser = expresionParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_handler)

        tree = parser.root()

        # Verificación de Errores Léxicos/Sintácticos
        if error_handler.tiene_errores():
            print("\nSe encontraron errores en el análisis inicial:")
            for err in error_handler.errores: 
                print(err)
            return

        semantic_checker = SemanticVisitor()
        # visit devuelve la lista de errores acumulados
        errores_semanticos = semantic_checker.visit(tree)

        if errores_semanticos:
            print("\nERRORES SEMÁNTICOS ENCONTRADOS")
            for err in errores_semanticos: 
                print(err)
            print("\nEjecución cancelada por errores semánticos.")
            return

        # Intérprete / Ejecución
        print("Validación exitosa. Iniciando Intérprete...\n")
        
        interpreter = Visitor()
        try:
            interpreter.visit(tree)
            print("\nEjecución finalizada con éxito")
        except Exception as e:
            print(f"\n[Error de Ejecución]: {e}")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
    except Exception as e:
        print(f"Error inesperado en el Pipeline: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_pipeline(sys.argv[1])
    else:
        run_pipeline("entrada.txt")