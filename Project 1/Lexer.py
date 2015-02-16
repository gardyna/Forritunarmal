from Token import *

__author__ = 'Dagur'

import sys
import re


# note to self: this class really could have just been a function/generator
class Lexer(object):
	def __init__(self):
		self.input = re.split('(\W)', sys.stdin.read())
		self.input = list(filter(lambda a: a != '' and a != ' ' and a != '\n', self.input))

	def nextToken(self):
		"""
		Generator yielding tokens until it reaches EOF in standard input

		:return: Token
		"""
		for word in self.input:
			if re.search("[A-Z,a-z]", word):  	     # ID
				yield Token(word, "ID")
			elif word == "=":						 # ASSIGN
				yield Token(word, "ASSIGN")
			elif re.search("[0-9]+", word): 		 # INT
				yield Token(word, "INT")
			elif word == "END":  					 # END
				yield Token(word, "END")
			elif word == "+":  						 # PLUS
				yield Token(word, "PLUS")
			elif word == "-":  						 # MINUS
				yield Token(word, "MINUS")
			elif word == "*":  						 # MULT
				yield Token(word, "MULT")
			elif word == "(":  						 # LPAREN
				yield Token(word, "LPAREN")
			elif word == ")":  						 # RPAREN
				yield Token(word, "RPAREN")
			elif word == "print": 					 # PRINT
				yield Token(word, "PRINT")
			elif word == ";":						 # SEMICOL
				yield Token(word, "SEMICOL")
			else:  # ERROR
				return Token(word, "ERROR")

if __name__ == "__main__":
	#only need this package for testing
	import io
	print("mocking stdin")
	file = open("tests.txt")
	string = "".join(file.readlines())
	sys.stdin = io.StringIO(string)
	print("Creating lexer")
	lex = Lexer()
	print("asking for tokens and printing them")
	for token in lex.nextToken():
		print(token.lexene, token.tCode)
	print("\nresetting stdin")
	sys.stdin = sys.__stdin__
