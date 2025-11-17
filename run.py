from antlr4 import *
from DeepLearningLexer import DeepLearningLexer
from DeepLearningParser import DeepLearningParser
from DeepLearningVisitorImpl import DeepLearningVisitorImpl

input_stream = FileStream("test.dl", encoding="utf-8")
lexer = DeepLearningLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = DeepLearningParser(tokens)

tree = parser.program()
visitor = DeepLearningVisitorImpl()
# Ejecuta el arbol:
tree.accept(visitor)
