from armcompiler.parser.ArmYacc import *
y = ArmSyntaticPatternParser()
y.build()
code = '''
         addr1 EQU 0x10

AREA main, CODE, READONLY

main PROC
	LDR R0, 0x35
	LDR R1, 0x12
		ADDS R2, R0, R1    ; teste tesssste
	SUBS R3, R0, R1

	END'''
expr = y.parsing(code)
expr

'''
from armcompiler.translator.ArmTranslator import *
t = ArmTranslator()
code_list = t.get_instruction_binary_list(expr)
code_list
directive_list = t.get_directive_list(expr)
directive_list
instruction_list = t.get_instruction_list(code_list)
instruction_list


from armcompiler.lexer.ArmLexer import *
l = ArmLexer()
l.build()
code = '''
         addr1 EQU 0x10

AREA main, CODE, READONLY

main PROC
	LDR R0, 0x35
	LDR R1, 0x12
		ADDS R2, R0, R1    ; teste tesssste
	SUBS R3, R0, R1

	END'''
l.test(code)
l.test('    addr1 EQU 0x10;')
'''