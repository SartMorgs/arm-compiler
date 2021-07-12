import ply.yacc as yacc

# Get the token from the lexer
from armcompiler.lexer.ArmLexer import *

class ArmSyntaticPatternParser():
	lexer = ArmLexer()
	lexer.build()
	tokens = lexer.tokens

	def p_code(self, p):
		'''code : labels codetypes main functions interruptions END
				| codetypes main functions interruptions END
				| labels codetypes main functions END
				| codetypes main functions END
				| labels codetypes main END
				| codetypes main END'''
		if len(p) == 7:
			p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
		elif len(p) == 6:
			p[0] = (p[1], p[2], p[3], p[4], p[5])
		elif len(p) == 5:
			p[0] = (p[1], p[2], p[3], p[4])
		else:
			p[0] = (p[1], p[2], p[3])

	def p_main(self, p):
		'''main : FUNCTIONNAME PROC commands'''
		p[0] = (p[1], p[2], p[3])

	def p_commands(self, p):
		'''commands : command commands
					| command
		'''
		if len(p) == 3:
			p[0] = f'{p[1]} | {p[2]} |'
		else:
			p[0] = p[1]

	def p_labels(self, p):
		'''labels : label labels
				  | label'''
		if len(p) == 3:
			p[0] = f'{p[1]} | {p[2]}'
		else:
			p[0] = p[1]

	def p_codetypes(self, p):
		'''codetypes : codetype codetypes
					 | codetype'''
		if len(p) == 3:
			p[0] = f'{p[1]} | {p[2]} |'
		else:
			p[0] = p[1]

	def p_functions(self, p):
		'''functions : function functions
				  	 | function'''
		if len(p) == 3:
			p[0] = f'{p[1]} | {p[2]} |'
		else:
			p[0] = p[1]

	def p_interruptions(self, p):
		'''interruptions : interruption interruption
				  	 	 | interruption'''
		if len(p) == 3:
			p[0] = f'{p[1]} | {p[2]} |'
		else:
			p[0] = p[1]


	def p_label(self, p):
		'''label : ADDRESSNAME EQU NUMBER'''
		p[0] = (p[1], p[2], p[3])

	def p_codetype(self, p):
		'''codetype : AREA FUNCTIONNAME COMMA CODE COMMA AREATYPE'''
		p[0] = (p[1], p[2], p[4], p[6])

	def p_function(self, p):
		'''function : FUNCTIONNAME PROC commands ENDP'''
		p[0] = (p[1], p[2], p[3], p[4])

	def p_interruption(self, p):
		'''interruption : INTHANDLER PROC commands ENDP'''
		p[0] = (p[1], p[2], p[3], p[4])

	def p_command(self, p):
		'''command : OPCODE NUMBER
				   | OPCODE FUNCTIONNAME
				   | OPCODE body
				   | OPCODE'''
		if len(p) == 3:
			p[0] = (p[1], p[2])
		else:
			p[0] = p[1]

	def p_body(self, p):
		'''body : REGISTER COMMA REGISTER COMMA REGISTER
				| REGISTER COMMA REGISTER NUMBER
				| REGISTER COMMA NUMBER
				| REGISTER COMMA REGISTER
				| REGISTER'''
		if len(p) == 6:
			p[0] = f'{p[1]}; {p[3]}; {p[5]};'
		elif len(p) == 5:
			p[0] = f'{p[1]}; {p[3]}; {p[4]};'
		elif len(p) == 4:
			p[0] = f'{p[1]}; {p[3]};'
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