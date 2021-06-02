# Arm Translator

class ArmTranslator():

	def __init__(self):
		self.opcode = {
			'ADDS': ('000001', '1', '16'),
			'SUBS': ('000010', '1', '16'),
			'MULS': ('000011', '1', '16'),
			'ANDS': ('000100', '1', '16'),
			'ORRS': ('000101', '1', '16'),
			'EORS': ('000110', '1', '16'),
			'BICS': ('000111', '1', '16'),
			'ASRS': ('001000', '1', '16'),
			'LSLS': ('001001', '1', '16'),
			'LSRS': ('001010', '1', '16'),
			'RORS': ('001011', '1', '16'),
			'CMN': 	('001100', '2', '8'),
			'CMP': 	('001101', '2', '8'),
			'MOVS': ('001110', '4', ''),
			'BEQ': 	('001111', '3', '26'),
			'BNE': 	('010000', '3', '26'),
			'BLT': 	('010001', '3', '26'),
			'BL': 	('010010', '3', '26'),
			'BX': 	('010011', '3', '26'),
			'LDR': 	('010100', '4', '14'),
			'STR': 	('010101', '4', '14'),
			'NOP': 	('111111', '5', '0')
		}

		self.directives = ['EQU', 'ORG', 'END']

	def get_register(self, reg):
		register = int(reg.replace('R', ''))
		binary = bin(register).replace('0b', '')
		while len(binary) < 5:
			binary = '0' + binary
		return binary

	def get_number(self, value, optype='NOP'):
		length = int(self.opcode[optype][2])
		number = int(value)
		binary = bin(number).replace('0b', '')
		while len(binary) < length:
			binary = '0' + binary
		return binary

	def get_address(self, addr):
		address = ''.join(format(i, '08b') for i in bytearray(addr, encoding='utf-8'))
		return address

	def get_instruction_binary_list(self, expression):
		optype = 'NOP'
		code_list = []
		for exp in expression:
			instruction = []
			for inst in exp:
				dict_keys = [key for key in self.opcode.keys()]
				if inst in dict_keys:
					optype = inst
					instruction.append(self.opcode[optype][0])
				elif inst not in self.directives and not isinstance(inst, str):
					for field in inst:
						if 'R' in field:
							instruction.append(self.get_register(field))
						elif field.isnumeric():
							instruction.append(self.get_number(field, optype))
			if instruction:
				code_list.append(instruction)

		return code_list

	def get_directive_list(self, expression):
		direct_list = []
		for exp in expression:
			directive = []
			for inst in exp:
				if inst in self.directives:
					directive.append(inst)
				elif inst not in self.opcode:
					if isinstance(inst, str):
						directive.append(inst)

			if directive:
				direct_list.append(directive)

		return direct_list 					

	def get_instruction_list(self, code_list):
		instruction_list = []

		for clist in code_list:
			code = ''.join([str(item) for item in clist])

			while len(code) < 32:
				code = code + '0'

			instruction_list.append(code)

		return instruction_list
