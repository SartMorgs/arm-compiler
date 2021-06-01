from armcompiler.parser.ArmYacc import *
y = ArmSyntaticPatternParser()
y.build()
code = ['    LDR R0, 35;', 'LDR R1, 12;', 'ADDS R2, R0, R1;   #teste   ', 'SUBS R3, R0, R1;']
expr = y.parsing(code)

from armcompiler.translator.ArmTranslator import *
t = ArmTranslator()
t.get_instruction_body(expr)