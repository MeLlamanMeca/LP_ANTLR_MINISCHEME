import sys
from antlr4 import *
from generated.schemeLexer import schemeLexer
from generated.schemeParser import schemeParser
from treeVisitor import TreeVisitor
from myErrorListener import MyErrorListener

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scheme.py <filename>")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        input_stream = FileStream(file_name, encoding='utf-8')
        lexer = schemeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = schemeParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())
        tree = parser.root()
        visitor = TreeVisitor()
        visitor.visit(tree)
