import sys
from antlr4 import *
from gramatica_finalLexer import gramatica_finalLexer

codigo = 'program { print(42); }'
lexer = gramatica_finalLexer(InputStream(codigo))

for token in lexer.getAllTokens():
    print(f"Token: {token.text}, Tipo: {lexer.symbolicNames[token.type]}")
