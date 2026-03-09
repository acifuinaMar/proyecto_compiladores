from visitor import Visitor
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4 import ParserRuleContext
from expresionLexer import expresionLexer
from expresionParser import expresionParser

def print_tree(tree, parser, level=0):
    indent = "|   " * level

    if isinstance(tree, ParserRuleContext):
        rule_name = parser.ruleNames[tree.getRuleIndex()]
        print(f"{indent}|_ {rule_name}")
    else:
        print(f"{indent}|_ {tree.getText()}")

    for i in range(tree.getChildCount()):
        print_tree(tree.getChild(i), parser, level + 1)

input_stream = FileStream('entrada.txt', encoding='utf-8')
lexer = expresionLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = expresionParser(token_stream)

tree = parser.root()
visitor = Visitor()
resultado = visitor.visit(tree)

print("\nResultado:", resultado)

print_tree(tree, parser)