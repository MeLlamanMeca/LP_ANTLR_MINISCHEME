import sys

from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax error at line {line}, column {column}: {msg}", file=sys.stderr)
        sys.exit(1)
