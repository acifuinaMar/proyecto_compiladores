from visitor import Visitor
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4 import ParserRuleContext
from expresionLexer import expresionLexer
from expresionParser import expresionParser
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error de sintaxis en línea {line}, columna {column}: {msg}")


# Función para imprimir el árbol
def print_tree(tree, parser, level=0):
    indent = "|   " * level

    if isinstance(tree, ParserRuleContext):
        rule_name = parser.ruleNames[tree.getRuleIndex()]
        print(f"{indent}|_ {rule_name}")
    else:
        
        print(f"{indent}|_ {tree.getText()}")

    for i in range(tree.getChildCount()):
        print_tree(tree.getChild(i), parser, level + 1)


def main():
    try:
        # Leer archivo de entrada
        input_stream = FileStream('entrada.txt', encoding='utf-8')

        # Lexer
        lexer = expresionLexer(input_stream)

        # Tokens
        token_stream = CommonTokenStream(lexer)

        # Parser
        parser = expresionParser(token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        # Árbol sintáctico
        tree = parser.root()

        # Visitor
        visitor = Visitor()
        resultado = visitor.visit(tree)

        # Salida
        print("\n===== RESULTADO =====")
        print(resultado)

        print("\n===== ÁRBOL =====")
        print_tree(tree, parser)

    except Exception as e:
        print("\nERROR:")
        print(e)


if __name__ == '__main__':
    main()