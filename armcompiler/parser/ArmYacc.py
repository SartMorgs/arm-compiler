import ply.yacc as yacc

# Get the token from the lexer
from armcompiler.lexer.ArmLexer import *

class ArmSyntaticPatternParser():
	lexer = ArmLexer()
	lexer.build()
	tokens = lexer.tokens

	def p_code(self, p):
		'''code : directives main functions interruptions END
				| directives main interruptions END
				| directives main functions END
				| directives main END'''
		if len(p) == 6:
			p[0] = (p[1], p[2], p[3], p[4], p[5])
		elif len(p) == 5:
			p[0] = (p[1], p[2], p[3], p[4])
		else:
			p[0] = (p[1], p[2], p[3])

	def p_directives(self, p):
		'''directives : directive'''
		p[0] = p[1]

	def p_main(self, p):
		'''main : FUNCTIONNAME PROC command'''
		p[0] = p[1]

	def p_functions(self, p):
		'''functions : function'''
		p[0] = p[1]

	def p_interruptions(self, p):
		'''interruptions : interruption'''
		p[0] = p[1]

	def p_directive(self, p):
		'''directive : AREA FUNCTIONNAME COMMA CODE AREATYPE
					 | ADDRESSNAME EQU NUMBER
					 | directive
					 | '''
		if len(p) == 6:
			p[0] = (p[1],  p[2],  p[4], p[5])
		elif len(p) == 4:
			p[0] = (p[1], p[2], p[3])
		else:
			p[0] = p[1]


	def p_function(self, p):
		'''function : FUNCTIONNAME PROC command ENDP
					| function
					| '''
		if len(p) == 5:
			p[0] = (p[1], p[2], p[3], p[4])
		else:
			p[0] = p[1]

	def p_interruption(self, p):
		'''interruption : INTHANDLER PROC command ENDP
						| interruption
						| '''
		if len(p) == 5:
			p[0] = (p[1], p[2], p[3], p[4])
		else:
			p[0] = p[1]

	def p_command(self, p):
		'''command : OPCODE NUMBER
				   | OPCODE FUNCTIONNAME
				   | OPCODE body
				   | OPCODE
				   | command
				   | '''
		if len(p) == 3:
			p[0] = (p[1], p[2])
		elif len(p) == 2:
			p[0] = p[1]
		else:
			p[0] = p[1]

	def p_body(self, p):
		'''body : REGISTER COMMA REGISTER COMMA REGISTER
				| REGISTER COMMA REGISTER NUMBER
				| REGISTER COMMA NUMBER
				| REGISTER COMMA REGISTER
				| REGISTER
				| '''
		if len(p) == 6:
			p[0] = (p[1], p[3], p[5])
		elif len(p) == 5:
			p[0] = (p[1], p[3], p[4])
		elif len(p) == 4:
			p[0] = (p[1], p[3])
		else:
			p[0] = p[1]

	# Error rule for syntax errors
	def p_error(self, p):
		if p:
			print(f'Syntax error: unexpected token type={p.type} with value={p.value} at position {p.lexer.lexpos}')
		else:
			print('Syntax error at EOF')

	# Build the parser
	def build(self, **kwargs):
		self.parser = yacc.yacc(module=self, **kwargs)

	def parsing(self, data):
		result = self.parser.parse(data)
		print(result)
		return result
		'''
		parser_result = []
		for line in data:
			result = self.parser.parse(line)
			parser_result.append(result)
		return parser_result
		'''

	def test(self):
		while True:
			try:
				s = input('Código >')
			except EOFError:
				break;
			if not s: continue
			result = self.parser.parse(s)
			print(result)