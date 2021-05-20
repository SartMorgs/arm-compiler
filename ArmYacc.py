import ply.yacc as yacc

# Get the token mar from the lexer
from ArmLexer import *

class ArmSyntaticPatternParser(object):
	def p_command(self, p):
		'''command : ADDRESSNAME OPCODE NUMBER SEMICOLON
				| OPCODE NUMBER SEMICOLON
				| OPCODE body
				| OPCODE'''
		if len(p) == 5:
			p[0] = (p[1], p[2], p[3])
		elif len(p) == 4:
			p[0] = (p[1], p[2])
		elif len(p) == 3:
			p[0] = (p[1], p[2])
		else:
			p[0] = p[1]


	def p_body(self, p):
		'''body : REGISTER COMMA REGISTER COMMA REGISTER SEMICOLON
			| REGISTER COMMA REGISTER NUMBER SEMICOLON
			| REGISTER COMMA NUMBER SEMICOLON
			| REGISTER COMMA REGISTER SEMICOLON
			| REGISTER SEMICOLON'''
		if len(p) == 7:
			p[0] = (p[1], p[3], p[5])
		elif len(p) == 6:
			p[0] = (p[1], p[3], p[4])
		elif len(p) == 5:
			p[0] = (p[1], p[3])
		else:
			p[0] = p[1]

	# Error rule for syntax errors
	def p_error(self, p):
		print(f'Syntax error: unexpected token type={p.type} with value={p.value} at position {p.lexer.lexpos}')

	# Build the parser
	def build(self, **kwargs):
		self.parser = yacc.yacc(module=self, **kwargs)

	def test(self, data):
		while True:
			try:
				s = input('Código >')
			except EOFError:
				break;
			if not s: continue
			result = self.parser.parse(s)
			print(result)