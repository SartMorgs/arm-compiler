from armcompiler.parser.ArmYacc import *
y = ArmSyntaticPatternParser()
y.build()
code = ['	LDR R0, 35;', '	LDR R1, 12;', '		ADDS R2, R0, R1;    # teste tesssste', '	SUBS R3, R0, R1;', '     addr1 EQU 10;']
expr = y.parsing(code)
expr

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
l.test('     EQU addr1 10;')