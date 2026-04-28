from antlr4 import *
from gramatica_finalLexer import gramatica_finalLexer
from gramatica_finalParser import gramatica_finalParser
from custom_errors import ANTLRErrorListener

class ParserPhase:
    def __init__(self, error_handler):
        self.error_handler = error_handler
    
    def ejecutar(self, codigo):
        try:
            lexer = gramatica_finalLexer(InputStream(codigo))
            lexer.removeErrorListeners()
            lexer.addErrorListener(ANTLRErrorListener(self.error_handler))
            
            stream = CommonTokenStream(lexer)
            parser = gramatica_finalParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(ANTLRErrorListener(self.error_handler))
            
            tree = parser.root()
            
            return not self.error_handler.tiene_errores(), tree
        except Exception as e:
            self.error_handler.error_sintactico(0, 0, str(e))
            return False, None