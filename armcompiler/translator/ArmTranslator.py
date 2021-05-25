# Arm Translator

class ArmTranslater():
	opcode = {
		'ADDS': ('000001', '1', '16')
		'SUBS': ('000010', '1', '16')
		'MULS': ('000011', '1', '16')
		'ANDS': ('000100', '1', '16')
		'ORRS': ('000101', '1', '16')
		'EORS': ('000110', '1', '16')
		'BICS': ('000111', '1', '16')
		'ASRS': ('001000', '1', '16')
		'LSLS': ('001001', '1', '16')
		'LSRS': ('001010', '1', '16')
		'RORS': ('001011', '1', '16')
		'CMN': 	('001100', '2', '8')
		'CMP': 	('001101', '2', '8')
		'MOVS': ('001110', '4', '')
		'BEQ': 	('001111', '3', '26')
		'BNE': 	('010000', '3', '26')
		'BLT': 	('010001', '3', '26')
		'BL': 	('010010', '3', '26')
		'BX': 	('010011', '3', '26')
		'LDR': 	('010100', '4', '14')
		'STR': 	('010101', '4', '14')
		'NOP': 	('111111', '5', '0')
	}

	def get_register(self, reg):
		reg = int(register.replace('R', ''))
		binary = bin(reg).replace('0b', '')
		while len(binary) < 5:
			binary = '0' + binary
		return binary

	def get_number(self, value, optype):
		length = int(optype)
		number = int(value)
		binary = bin(number).replace('0b', '')
		while len(binary) < length:
			binary = '0' + binary
		return binary

	def get_instruction_body(self, expression):
		for exp in expression:
			if isinstance(exp, tuple):
				registers = [get_register(field) for field in exp if field.contains('R')]
				registers = [get_number(field) for field in exp if !field.contains('R')]
