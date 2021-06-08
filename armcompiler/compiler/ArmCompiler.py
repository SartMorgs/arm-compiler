from armcompiler.lexer.ArmLexer import *
from armcompiler.parser.ArmYacc import *
from armcompiler.translator.ArmTranslator import *

class ArmCompiler():
	def __init__(self, multiline_code):
		# Define lexer
		self.lex = ArmLexer()

		# Define parser
		self.yacc = ArmSyntaticPatternParser()

		# Define translator
		self.translator = ArmTranslator()

		# Define input code
		self.multiline_code = multiline_code
		self.list_code = []

	def set_multiline_code(code):
		self.multiline_code = code

	def build(self):
		self.lex.build()
		self.yacc.build()

		for line in self.multiline_code.split('\n'):
			self.list_code.append(line)

	def get_instruction_list(self):
		expr = self.yacc.parsing(self.list_code)
		code_list = self.translator.get_instruction_binary_list(expr)
		instruction_list = self.translator.get_instruction_list(code_list)

		return instruction_list

	def get_directive_list(self):
		expr = self.yacc.parsing(self.list_code)
		directive_list = self.translator.get_directive_list(expr)

		return directive_list