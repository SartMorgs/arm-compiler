import unittest
import armcompiler.app.parser.ArmYacc as ps

class TestArmSyntaticPatternParser(unittest.TestCase):

	def test_parsing_sample_load_sub(self):
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

			INT0_Handler   PROC
				SUBS R3, R0, R1
				SUBS R3, R0, R1
				ENDP
				END'''

		want = (
			('addr1', 'EQU', '0x10'), 
			('AREA', 'main', 'CODE', 'READONLY'), 
			('main', 'PROC', "('LDR', 'R0; 0x35;') | ('LDR', 'R1; 0x12;') | ('ADDS', 'R2; R0; R1;') | ('SUBS', 'R3; R0; R1;') | ('BL', 'func1') | ('B', 'main') | | | | |"), 
			('func1', 'PROC', "('LDR', 'R1; 0x12;') | ('ADDS', 'R2; R0; R1;') |", 'ENDP'), 
			('INT0_Handler', 'PROC', "('SUBS', 'R3; R0; R1;') | ('SUBS', 'R3; R0; R1;') |", 'ENDP'), 
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_code_with_comments(self):
		code = '''
		AREA main, CODE, READONLY
		; sadsadasdasdasd

		main PROC
			;sadasdasdasd sadsadas
			LDR R0, 0x35 ;asdsad
			SUBS R4, R0 0x12    ; teste tesssste
		END

		;sfg,fdlçgfd
		'''
		want = ( 
			('AREA', 'main', 'CODE', 'READONLY'), 
			('main', 'PROC', "('LDR', 'R0; 0x35;') | ('SUBS', 'R4; R0; 0x12;') |"), 
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_arithmetic_adds_type_2(self):
		code = '''
		         addr1 EQU 0x25

			AREA main, CODE, READONLY

			main PROC
				LDR R0, 0x35
					ADDS R2, R0 0x12    ; teste tesssste
				END'''

		want = (
			('addr1', 'EQU', '0x25'), 
			('AREA', 'main', 'CODE', 'READONLY'), 
			('main', 'PROC', "('LDR', 'R0; 0x35;') | ('ADDS', 'R2; R0; 0x12;') |"), 
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_arithmetic_subs_type_2(self):
		code = '''
		AREA main, CODE, READONLY

		main PROC
			LDR R0, 0x35
			SUBS R4, R0 0x12    ; teste tesssste
		END
		'''

		want = ( 
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R0; 0x35;') | ('SUBS', 'R4; R0; 0x12;') |"), 
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_comparison_cmn_type_1(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			LDR R5, -0x11
			LDR R4, -0x11
			CMN R5, R4
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; -0x11;') | ('LDR', 'R4; -0x11;') | ('CMN', 'R5; R4;') | |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_comparison_cmn_type_2(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			LDR R5, -0x11
			CMN R5, -0x11
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; -0x11;') | ('CMN', 'R5; -0x11;') |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_comparison_cmp_type_1(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			LDR R5, 0x15
			LDR R4, 0x15
			CMP R5, R4
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('LDR', 'R4; 0x15;') | ('CMP', 'R5; R4;') | |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_comparison_cmp_type_2(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			LDR R5, 0x15
			CMP R5, 0x15
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('CMP', 'R5; 0x15;') |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_movs_type_1(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			LDR R5, 0x15
			MOVS R4, R5
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('MOVS', 'R4; R5;') |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_movs_type_2(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			MOVS R4, 0x15
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', ('MOVS', 'R4; 0x15;')),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_beq_type1(self):
		code = '''
		addr1 EQU 0x10
		AREA main, CODE, READONLY

		main PROC
			MOVS R4, 0x15
			BEQ R4
		END
		'''
		
		want = (
			('addr1', 'EQU', '0x10'),
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BEQ', 'R4') |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_beq_type_2(self):
		code = '''
		addr1 EQU 0x10
		AREA main, CODE, READONLY

		main PROC
			MOVS R4, 0x15
			BEQ addr1
		END
		'''

		want = (
			('addr1', 'EQU', '0x10'),
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BEQ', 'addr1') |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_blt_type_2(self):
		code = '''
		AREA main, CODE, READONLY

		main PROC
			MOVS R4, 0x15
			BLT addr1
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BLT', 'addr1') |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_bl_type_2(self):
		code = '''
		AREA main, CODE, READONLY

		main PROC
			MOVS R4, 0x15
			BLT move_and_compare
		
		move_and_compare PROC
			LDR R4, 0x15
			MOVS R5, R4
			CMN R5, R4
			ENDP
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BLT', 'move_and_compare') |"),
			('move_and_compare', 'PROC', "('LDR', 'R4; 0x15;') | ('MOVS', 'R5; R4;') | ('CMN', 'R5; R4;') | |",'ENDP'),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_bx_type_1(self):
		code = '''
		AREA main, CODE, READONLY

		main PROC
			MOVS R4, 0x15
			BLT move_and_compare
			BX R14

		move_and_compare PROC
			LDR R4, 0x15
			MOVS R5, R4
			CMN R5, R4
			ENDP
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('BLT', 'move_and_compare') | ('BX', 'R14') | |"),
			('move_and_compare', 'PROC', "('LDR', 'R4; 0x15;') | ('MOVS', 'R5; R4;') | ('CMN', 'R5; R4;') | |",'ENDP'),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_nop(self):
		code = '''
		AREA main, CODE, READONLY

		main PROC
			NOP
			NOP

		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "NOP | NOP |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_bypass_b_type_1(self):
		code = '''
		AREA main, CODE, READONLY

		main PROC
			MOVS R4, 0x15
			B main

		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('MOVS', 'R4; 0x15;') | ('B', 'main') |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)


	def test_parsing_store_type_1(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			LDR R5, 0x15
			LDR R4, 0x15
			CMN R5, R4
			STR R4, R1
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('LDR', 'R4; 0x15;') | ('CMN', 'R5; R4;') | ('STR', 'R4; R1;') | | |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

	def test_parsing_store_type_2(self):
		code = '''
		AREA main, CODE, READONLY
		main PROC
			LDR R5, 0x15
			LDR R4, 0x15
			CMN R5, R4
			STR R4, 0x21
		END
		'''

		want = (
			('AREA', 'main', 'CODE', 'READONLY'),
			('main', 'PROC', "('LDR', 'R5; 0x15;') | ('LDR', 'R4; 0x15;') | ('CMN', 'R5; R4;') | ('STR', 'R4; 0x21;') | | |"),
			'END'
		)

		parser = ps.ArmSyntaticPatternParser()
		parser.build()

		got = parser.parsing(code)
		error_message = f'\nWanted value \n{want} \nis not equal to gotted value \n{got}'

		self.assertEqual(want, got, error_message)

if __name__ == '__main__':
	unittest.main()