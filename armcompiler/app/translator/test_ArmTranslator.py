import unittest
import armcompiler.app.translator.ArmTranslator as tr

class TestArmTranslator(unittest.TestCase):
	def test_translating_sample_load_sub(self):
		expr = (
			('addr1', 'EQU', '0x10'), 
			('AREA', 'main', 'CODE', 'READONLY'), 
			('main', 'PROC', "('LDR', 'R0; 0x35;') | ('LDR', 'R1; 0x12;') | ('ADDS', 'R2; R0; R1;') | ('SUBS', 'R3; R0; R1;') | ('BL', 'func1') | ('B', 'main') | | | | |"), 
			('func1', 'PROC', "('LDR', 'R1; 0x12;') | ('ADDS', 'R2; R0; R1;') |", 'ENDP'), 
			('INT0_Handler', 'PROC', "('SUBS', 'R3; R0; R1;') | ('SUBS', 'R3; R0; R1;') |", 'ENDP'), 
			'END'
		)

		want = {
			'main': [
				'11010000000000000001101010000000', 
				'11010000001000000000100100000000', 
				'00000100010000000000100000000000', 
				'00001000011000000000100000000000', 
				'110101F1F00000000000000000000000', 
				'011011F0F00000000000000000000000'
			], 
			'func1': [
				'11010000001000000000100100000000', 
				'00000100010000000000100000000000'
			], 
			'INT0_Handler': [
				'00001000011000000000100000000000', 
				'00001000011000000000100000000000'
			]
		} 

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_arithmetic_adds_type_2(self):
		expr = (
			('addr1', 'EQU', '0x25'), 
			('AREA', 'main', 'CODE', 'READONLY'), 
			('main', 'PROC', "('LDR', 'R0; 0x35;') | ('ADDS', 'R2; R0; 0x12;') |"), 
			'END'
		)

		want = {
			'main': [
				'11010000000000000001101010000000',
				'10000100010000000000000000010010'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_arithmetic_subs_type_2(self):
		expr = ( 
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R0; 0x35;') | ('SUBS', 'R4; R0; 0x12;') |"), 
			'END'
		)

		want = {
			'main': [
				'11010000000000000001101010000000',
				'10001000100000000000000000010010'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_arithmetic_comparison_cmn_type_1(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; -0x11;') | ('LDR', 'R4; -0x11;') | ('CMN', 'R5; R4;') | |"),
			'END'
		)

		want = {
			'main': [
				'11010000101000000000011110000000',
				'11010000100000000000011110000000',
				'00110000101001000000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_comparison_cmn_type_2(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; -0x11;') | ('CMN', 'R5; -0x11;') |"),
			'END'
		)

		want = {
			'main': [
				'11010000101000000000011110000000',
				'10110000101000011110000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_comparison_cmp_type_1(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('LDR', 'R4; 0x15;') | ('CMP', 'R5; R4;') | |"),
			'END'
		)

		want = {
			'main': [
				'11010000101000000000101010000000',
				'11010000100000000000101010000000',
				'00110100101001000000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_comparison_cmp_type_2(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('CMP', 'R5; 0x15;') |"),
			'END'
		)

		want = {
			'main': [
				'11010000101000000000101010000000',
				'10110100101000101010000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_bypass_move_type_1(self):
		expr = want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('MOVS', 'R4; R5;') |"),
			'END'
		)

		want = {
			'main': [
				'11010000101000000000101010000000',
				'00111000100001010000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_load_and_store_movs_type_2(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', ('MOVS', 'R4; 0x15;')),
			'END'
		)

		want = {
			'main': [
				'10111000100000000000101010000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_load_and_store_movs_type_1(self):
		expr = (
			('addr1', 'EQU', '0x10'),
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BEQ', 'R4') |"),
			'END'
		)

		want = {
			'main': [
				'10111000100000000000101010000000',
				'00111100100000000000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	'''
	def test_translate_bypass_beq_type_2(self):
		expr = (
			('addr1', 'EQU', '0x10'),
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BEQ', 'addr1') |"),
			'END'
		)

		want = {
			'main': [
				'10111000100000000000101010000000',
				'10111100000000000000000000010000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)
	

	// def test_translate_bypass_blt_type_2(self):


	'''

	def test_translate_bypass_bl_type_2(self):
		expr = want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BLT', 'move_and_compare') |"),
			('move_and_compare', 'PROC', "('LDR', 'R4; 0x15;') | ('MOVS', 'R5; R4;') | ('CMN', 'R5; R4;') | |",'ENDP'),
			'END'
		)

		want = {
			'main': [
				'10111000100000000000101010000000',
				'010001F1F00000000000000000000000'
			],
			'move_and_compare': [
				'11010000100000000000101010000000',
				'00111000101001000000000000000000',
				'00110000101001000000000000000000'	
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_bypass_bx_type_1(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BLT', 'move_and_compare') | ('BX', 'R14') | |"),
			('move_and_compare', 'PROC', "('LDR', 'R4; 0x15;') | ('MOVS', 'R5; R4;') | ('CMN', 'R5; R4;') | |",'ENDP'),
			'END'
		)

		want = {
			'main': [
				'10111000100000000000101010000000',
				'010001F1F00000000000000000000000',
				'01001101110000000000000000000000'
			],
			'move_and_compare': [
				'11010000100000000000101010000000',
				'00111000101001000000000000000000',
				'00110000101001000000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_nop(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "NOP | NOP |"),
			'END'
		)

		want = {
			'main': [
				'11111100000000000000000000000000',
				'11111100000000000000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_bypass_b_type_1(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('B', 'main') |"),
			'END'
		)

		want = {
			'main': [
				'10111000100000000000101010000000',
				'011011F0F00000000000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_store_type_1(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('LDR', 'R4; 0x15;') | ('CMN', 'R5; R4;') | ('STR', 'R4; R1;') | | |"),
			'END'
		)

		want = {
			'main': [
				'11010000101000000000101010000000',
				'11010000100000000000101010000000',
				'00110000101001000000000000000000',
				'01010100100000010000000000000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_translate_store_type_2(self):
		expr = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('LDR', 'R4; 0x15;') | ('CMN', 'R5; R4;') | ('STR', 'R4; 0x21;') | | |"),
			'END'
		)

		want = {
			'main': [
				'11010000101000000000101010000000',
				'11010000100000000000101010000000',
				'00110000101001000000000000000000',
				'11010100100000000001000010000000'
			]
		}

		translator = tr.ArmTranslator()
		instructions_blocks = translator.get_instruction_parsed_splited(expr)
		got = translator.get_instruction_binary_list(instructions_blocks) 

		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

if __name__ == '__main__':
	unittest.main()