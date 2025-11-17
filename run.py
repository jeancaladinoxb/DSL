from antlr4 import *
from DeepLearningLexer import DeepLearningLexer
from DeepLearningParser import DeepLearningParser

input_stream = FileStream("test.dl", encoding="utf-8")
lexer = DeepLearningLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = DeepLearningParser(tokens)

tree = parser.program()
print(tree.toStringTree(recog=parser))

