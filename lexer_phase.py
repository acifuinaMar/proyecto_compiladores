from antlr4 import *
from gramatica_finalLexer import gramatica_finalLexer
from custom_errors import ANTLRErrorListener

class LexerPhase:
    def __init__(self, error_handler):
        self.error_handler = error_handler
    
    def ejecutar(self, codigo):
        try:
            lexer = gramatica_finalLexer(InputStream(codigo))
            error_listener = ANTLRErrorListener(self.error_handler)
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            
            tokens = []
            token = lexer.nextToken()
            while token.type != Token.EOF:
                tokens.append({
                    "tipo": lexer.symbolicNames[token.type] if token.type >= 0 and token.type < len(lexer.symbolicNames) else str(token.type),
                    "texto": token.text,
                    "linea": token.line,
                    "columna": token.column
                })
                token = lexer.nextToken()
            
            return not self.error_handler.tiene_errores(), tokens
        except Exception as e:
            self.error_handler.error_lexico(0, 0, str(e))
            return False, []