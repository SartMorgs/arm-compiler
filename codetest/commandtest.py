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

func1 PROC
	LDR R1, 0x12
		ADDS R2, R0, R1    ; teste tesssste
	ENDP

INT0_Handler	PROC
	SUBS R3, R0, R1
	SUBS R3, R0, R1
	ENDP
	END'''
expr = y.parsing(code)
expr

from armcompiler.translator.ArmTranslator import *
t = ArmTranslator()
instructions_blocks = t.get_instruction_parsed_splited(expr)
instructions_blocks
binary_list = t.get_instruction_binary_list(instructions_blocks)  
binary_list
directive_list = t.get_directive_list(instructions_blocks)
directive_list
'''




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