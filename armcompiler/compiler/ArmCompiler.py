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


	def build(self):
		try:
			self.lex.build()
			self.yacc.build()
		except Exception as e:
			print(str(e))

	def compilation(self):
		try:
			expr = self.yacc.parsing(self.multiline_code)

			instructions_blocks = self.translator.get_instruction_parsed_splited(expr)
			self.instruction_list = self.translator.get_instruction_binary_list(instructions_blocks)
			self.directive_list = self.translator.get_directive_list(instructions_blocks)
		except Exception as e:
			print(str(e))

		return "Code compilation make successfully!"

	def get_instruction_list(self):
		return self.instruction_list

	def get_directive_list(self):
		return self.directive_list

if __name__ == '__main__':
	code = '''
         addr1 EQU 0x10

			AREA main, CODE, READONLY

			main PROC
				LDR R0, 0x35
				LDR R1, 0x12
					ADDS R2, R0, R1    ; teste tesssste
				SUBS R3, R0, R1
				BL func1
				B main

			func1 PROC
				LDR R1, 0x12
					ADDS R2, R0, R1    ; teste tesssste
				ENDP

			INT0_Handler	PROC
				SUBS R3, R0, R1
				SUBS R3, R0, R1
				ENDP
				END'''

	arm_compiler = ArmCompiler(code)
	arm_compiler.build()
	arm_compiler.compilation()
	print(arm_compiler.get_instruction_list())
	print(arm_compiler.get_directive_list())