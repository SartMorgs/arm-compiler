# module: tokrules.py
# This module just contains the lexing rules

# The lex.py module is used to brak input text into a collection of tokens specified by a collection of regular expression rules.
# yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar

import ply.lex as lex
import re

class ArmLexer():
	# List of tokens names
	tokens = [
		'EQU', 'AREA', 'END', 'ENDP', 'CODE', 'ORG', 'PROC', 'AREATYPE', 'INTHANDLER',
		'COMMA', 'REGISTER', 'FUNCTIONNAME', 'ADDRESSNAME', 'NUMBER', 'OPCODE'
	]

	# Regular expression rules for simples tokens
	t_EQU = r'\bEQU\b'
	t_AREA = r'\bAREA\b'
	t_END = r'\bEND\b'
	t_ENDP = r'\bENDP\b'
	t_CODE = r'\bCODE\b'
	t_ORG = r'\bORG\b'
	t_PROC = r'\bPROC\b'

	t_COMMA = r'\,'
	t_REGISTER = r'\bR[0-9]+\b'
	t_NUMBER = r'\b0x[0-9]+'

	t_OPCODE = r'\bADDS\b|\bSUBS\b|\bMULS\b|\bANDS\b|\bORRS\b|\bEORS\b|\bBICS\b|\bASRS\b|\bLSLS\b|\bLSRS\b|\bRORS\b|\bCMN\b|\bCMP\b|\bMOVS\b|\bBEQ\b|\bBNE\b|\bBLT\b|\bBL\b|\bBX\b|\bLDR\b|\bSTR\b|\bNOP\b'

	t_AREATYPE = r'\bREADONLY\b|\bREADWRITE\b'

	t_INTHANDLER = r'\bINT0_Handler\b|\bINT1_Handler\b|\bINT2_Handler\b|\bINT3_Handler\b|\bINT4_Handler\b|\bINT5_Handler\b|\bINT6_Handler\b|\bINT7_Handler\b|\bINT8_Handler\b|\bINT9_Handler\b|\bINT10_Handler\b|\bINT11_Handler\b|\bINT12_Handler\b|\bINT13_Handler\b|\bINT14_Handler\b|\bINT15_Handler\b|\bINT16_Handler\b'
	
	t_ADDRESSNAME = r'(\b[a-zA-Z_]+[a-zA-Z0-9_]*[^\sEQU|^\sAREA|^\sEND|^\sENDP|^\sCODE|^\sORG|^\sPROC|^\sREADONLY|^\sREADWRITE]\b)(?=\sEQU)' #([a-zA-Z_]+[a-zA-Z0-9_]*)
	t_FUNCTIONNAME = r'((\b[A-Za-z]+[A-Za-z0-9]*[^\sEQU|^\sAREA|^\sEND|^\sENDP|^\sCODE|^\sORG|^\sPROC|^\sREADONLY|^\sREADWRITE]\b))(?!\sEQU)' #(?<!\#.*) (?:\sEQU)

	def t_newline(self, t):
		r'\n+'
		t.lexer.lineno += len(t.value)

	def t_error(self, t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

	# Ignored characters
	t_ignore = '\t+| +|\r+'
	t_ignore_comments = r'[;][^\n]*'

	# Compute column
	#	input is the input text string
	#	token is a token instance
	def find_column(self, input, token):
		line_start = input.rfind('\n', 0, token.lexpos) + 1
		return (token.lexpos - line_start) + 1

	# Test it output
	def test(self, data):
		self.lexer.input(data)
		while True:
			tok = self.lexer.token()
			if not tok:
				break
			print(tok)

	# -----------------------------------------
	# Constructor
	# -----------------------------------------
	def build(self, **kwargs):
		self.lexer = lex.lex(module=self, **kwargs)