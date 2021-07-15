from armcompiler.lexer.ArmLexer import *
from armcompiler.parser.ArmYacc import *
from armcompiler.translator.ArmTranslator import *

import json

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
		self.instruction_list = {}
		self.directive_list = []

	def set_multiline_code(code):
		self.multiline_code = code

	def build(self):
		try:
			self.lex.build()
			self.yacc.build()
		except Exception as e:
			return e.message

	def compilation(self):
		try:
			expr = self.yacc.parsing(self.multiline_code)
		except Exception as e:
			return e.message

		try:
			instructions_blocks = self.translator.get_instruction_parsed_splited(expr)
			self.instruction_list = self.translator.get_instruction_binary_list(instructions_blocks)
			self.directive_list = self.translator.get_directive_list(instructions_blocks)
		except Exception as e:
			return e.message

		return "Code compilation make successfully!"

	def get_instruction_list(self):
		return self.instruction_list

	def get_directive_list(self):
		return self.directive_list