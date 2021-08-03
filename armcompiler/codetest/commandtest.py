import armcompiler.app.parser.ArmYacc as ps
y = ps.ArmSyntaticPatternParser()
y.build()
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
expr = y.parsing(code)
import armcompiler.app.translator.ArmTranslator as tr
t = tr.ArmTranslator()
instructions_blocks = t.get_instruction_parsed_splited(expr)
print(instructions_blocks)

binary_list = t.get_instruction_binary_list(instructions_blocks)  
print(binary_list)
directive_list = t.get_directive_list(instructions_blocks)
print(directive_list)