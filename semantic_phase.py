from semantic_visitor import SemanticVisitor

class SemanticPhase:
    def __init__(self, error_handler):
        self.error_handler = error_handler
        self.symbol_table = None
    
    def ejecutar(self, ast):
        if ast is None:
            self.error_handler.error_semantico(0, 0, "AST vacío")
            return False, None
        
        try:
            semantic = SemanticVisitor()
            semantic.visit(ast)
            
            # Transferir errores al manejador
            for error in semantic.errores:
                self.error_handler.error_semantico(0, 0, error)
            
            return not self.error_handler.tiene_errores(), semantic.tabla_tipos
        except Exception as e:
            self.error_handler.error_semantico(0, 0, str(e))
            return False, None