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
			'MOVS': ('001110', '4', '14'),
			'BEQ': 	('001111', '3', '26'),
			'BNE': 	('010000', '3', '26'),
			'BLT': 	('010001', '3', '26'),
			'BL': 	('010010', '3', '26'),
			'BX': 	('010011', '3', '26'),
			'LDR': 	('010100', '4', '14'),
			'STR': 	('010101', '4', '14'),
			'NOP': 	('111111', '5', '0'),
			'BL': ('110101', '3', '26'),
			'B': ('011011', '3', '26')
		}

		# 1 - Arithmetic
		# 2 - Comparison
		# 3 - Bypass
		# 4 - Load and Store

		self.reserved = ['EQU', 'ORG', 'AREA', 'CODE', 'READONLY', 'READWRITE', 'PROC', 'END', 'ENDP']

		self.addr_alias_mapping = {}
		self.addr_function_mapping = {}

	def twos_comp(self, val, bits):
		if (val & (1 << (bits - 1))) != 0:
			val = val - (1 << bits)
		return val 

	def get_register(self, reg):
		register = int(reg.replace('R', ''))
		binary = bin(register).replace('0b', '')
		while len(binary) < 5:
			binary = '0' + binary
		return binary

	def get_number(self, value, optype='NOP'):
		length = int(self.opcode[optype][2])
		number = int(value, 16)
		if number < 0:
			number = number * (-1)
			binary_string = bin(number).replace('0b', '')
			two_complement_number =  self.twos_comp(number, len(binary_string))
			binary = bin(two_complement_number).replace('0b', '').replace('-', '')
		else:
			binary = bin(number).replace('0b', '')
		while len(binary) < length:
			binary = '0' + binary
		return binary

	def get_address(self, addr):
		address = ''.join(format(i, '08b') for i in bytearray(addr, encoding='utf-8'))
		return address

	def get_instruction_parsed_splited(self, expression):
		instructions_blocks = {}
		function = ''

		instructions_blocks['directive'] = []

		for exp in expression:
			if 'PROC' in exp:
				function = exp[0]
			else:
				instructions_blocks['directive'].append(exp)
			for block in exp:
				if '|' in block:
					instructions_assembly = block.replace(';', ',').replace(' ', '').split('|')

					instructions_blocks[function] = instructions_assembly
				elif type(block) == tuple:
					item2 = block[1].replace(';', ',').replace(' ', '')
					instructions_blocks[function] = [f'(\'{block[0]}\', \'{item2}\')']

		return instructions_blocks

	def get_instruction_binary_list(self, expression):
		optype = 'NOP'
		dict_keys = [key for key in self.opcode.keys()]
		binary_code_list = {}

		self.build_addr_function_mapping(expression)

		for key, value in expression.items():
			if key != 'directive':
				binary_code_list[key] = []
				for iten in value:
					try:
						instruction_list = iten.replace('(', '').replace(')', '').replace('\'', '').split(',')
						instruction_list[:] = [item for item in instruction_list if item]
						instruction = ''
						if instruction_list:
							for inst_value in instruction_list:
								if inst_value in dict_keys:
									optype = inst_value
									instruction = instruction + self.opcode[inst_value][0]
									instruction_type = self.opcode[inst_value][1]
								elif 'R' in inst_value:
									instruction = instruction + self.get_register(inst_value)
								elif inst_value in self.addr_alias_mapping.keys():
									instruction = instruction + self.addr_alias_mapping[inst_value]
								elif inst_value in self.addr_function_mapping.keys():
									instruction = instruction + 'F' + self.addr_function_mapping[inst_value] + 'F'
								elif '0x' in inst_value:
									instruction = instruction + self.get_number(inst_value, optype)
									list_aux_instruction = list(instruction)
									list_aux_instruction[0] = '1'
									instruction = ''.join(list_aux_instruction)

							instuction_full_size = self.increase_instructions_with_zeros(instruction)
							binary_code_list[key].append(instuction_full_size)
					except Exception as e:
						print(str(e))

			else:
				self.build_addr_alias_mapping(value)

		return binary_code_list

	def get_directive_list(self, expression):
		direct_list = {}
		count = 1
		for key, value in expression.items():
			if key == 'directive' or key == 'addr_alias':
				for iten in value[:-1]:
					direct_list[str(count)] = iten
					count = count + 1
		return direct_list

	def increase_instructions_with_zeros(self, instruction):
		code = ''.join([str(item) for item in instruction])

		while len(code) < 32:
			code = code + '0'

		return code

	def build_addr_alias_mapping(self, alias_list):
		for iten in alias_list:
			if iten[1] == 'EQU':
				self.addr_alias_mapping[iten[0]] = iten[2]

		#print(self.addr_alias_mapping)

	def build_addr_function_mapping(self, expression):
		function_count = 0
		for key in expression.keys():
			if key != 'directive' and key != 'addr_alias':
				self.addr_function_mapping[key] = str(function_count)
				function_count += 1

		#print(self.addr_function_mapping)
