__author__ = 'Dagur'

from enum import Enum
TokenCodes = Enum('TokenCodes', 'ID ASSIGN SEMICOL INT PLUS MINUS MULT LPAREN RPAREN PRINT END ERROR')


class Token(object):
	def __init__(self, lexene, code):
		self.lexene = lexene
		self.tokenCode = TokenCodes[code].value

if __name__ == "__main__":
	print("The token codes are:", list(TokenCodes))
	print("Creating token with lexene = ID")
	token = Token("ID")
	print("token = ", token.lexene,token.tokenCode)