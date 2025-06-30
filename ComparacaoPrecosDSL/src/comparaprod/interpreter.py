from antlr4 import *
from .ComparaProdLexer import ComparaProdLexer
from .ComparaProdParser import ComparaProdParser
from .visitor import ComparaProdVisitorImpl

def interpret(input_text):
    input_stream = InputStream(input_text)
    lexer = ComparaProdLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComparaProdParser(stream)
    tree = parser.program()
    
    visitor = ComparaProdVisitorImpl()
    results = visitor.visit(tree)
    
    return results