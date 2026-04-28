from visitor import Visitor

class InterpreterPhase:
    def __init__(self, error_handler):
        self.error_handler = error_handler
    
    def ejecutar(self, ast):
        if ast is None:
            self.error_handler.error_ejecucion(0, 0, "AST vacío")
            return False, None
        
        try:
            visitor = Visitor()
            resultado = visitor.visit(ast)
            return not self.error_handler.tiene_errores(), resultado
        except Exception as e:
            self.error_handler.error_ejecucion(0, 0, str(e))
            return False, None