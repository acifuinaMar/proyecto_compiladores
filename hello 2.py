from visitor import Visitor
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from expresionLexer import expresionLexer
from expresionParser import expresionParser

def print_pretty_tree(tree, parser, indent="", is_last=True):
    marker = "└── " if is_last else "├── "
    if isinstance(tree, TerminalNodeImpl):
        node_name = f"token: {tree.getText()}"
    else:
        node_name = parser.ruleNames[tree.getRuleIndex()]

    # Filtro para no imprimir el token de fin de archivo si no es necesario
    if node_name != "token: <EOF>":
        print(indent + marker + node_name)
        new_indent = indent + ("    " if is_last else "│   ")
        child_count = tree.getChildCount()
        for i in range(child_count):
            is_last_child = (i == child_count - 1)
            print_pretty_tree(tree.getChild(i), parser, new_indent, is_last_child)

# --- Ejecución Principal ---
input_stream = FileStream('entrada.txt', encoding='utf-8')
lexer = expresionLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = expresionParser(token_stream)

tree = parser.root()

# 1. Ejecutar el Visitor PRIMERO para obtener los resultados
visitor = Visitor()
resultados = visitor.visit(tree)

# 2. Imprimir los resultados al inicio
if isinstance(resultados, list):
    # Si tienes varias sentencias, imprimimos la última o todas
    # Según tu imagen, parece que solo esperas un valor principal:
    print(f"Resultado: {resultados[-1] if resultados else 'N/A'}")
else:
    print(f"Resultado: {resultados}")

# 3. Imprimir el Árbol después
print_pretty_tree(tree, parser)