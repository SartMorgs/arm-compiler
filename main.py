from armcompiler.compiler.ArmCompiler import *

if __name__ == "__main__":
	# Just for test
	code = '''LDR R0, 35;
		LDR R1, 12;
				ADDS R2, R0, R1;    # teste tesssste
					SUBS R3, R0, R1;
					     addr1 EQU 10;
					arr2 EQU 005;'''

	armcompiler = ArmCompiler(code)
	armcompiler.build()
	print(armcompiler.get_directive_list())
	print(armcompiler.get_instruction_list())
