import ply.yacc as yacc

# Get the token mar from the lexer
from ArmLexer.ArmLexer import *

class ArmSyntaticPatternParser(object):
	def p_command(p):
		'''command:  OPCODE + body
					| ADDRESSNAME + OPCODE + NUMBER + SEMICOLON
					| OPCODE + NUMBER + SEMICOLON
					| OPCODE'''

	def p_body(p):
		'''body: REGISTER + COMMA + REGISTER + COMMA + REGISTER + SEMICOLON
				| REGISTER + COMMA + REGISTER + NUMBER + SEMICOLON
				| REGISTER + COMMA + NUMBER + SEMICOLON
				| REGISTER + COMMA + REGISTER + SEMICOLON
				| REGISTER + SEMICOLON'''

	# Error rule for syntax errors
	def p_error(p):
		print("Syntax error input!")

	# Build the parser
	parser = yacc.yacc()
