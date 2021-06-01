# module: tokrules.py
# This module just contains the lexing rules

# The lex.py module is used to brak input text into a collection of tokens specified by a collection of regular expression rules.
# yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar

import ply.lex as lex
import re

class ArmLexer():
	# List of tokens names
	tokens = [
		'COMMA', 'SEMICOLON', 'REGISTER', 'FUNCTIONNAME',
		'ADDRESSNAME', 'NUMBER', 'COMMENTS', 'OPCODE'
		]

	# Regular expression rules for simples tokens
	t_COMMA = r'\,'
	t_SEMICOLON = r'\;'
	t_REGISTER = r'\bR[0-9]+\b'
	t_FUNCTIONNAME = r'(?<!\#)([a-qs-zA-QS-Z_]+[a-zA-Z0-9_]*)' #(?<!\#.*)
	t_ADDRESSNAME = r'[a-zA-Z_]+[a-zA-Z0-9_]*(?=\sEQU.)'
	t_NUMBER = r'[0-9]+'

	# A regular expression rule with some action code
	def t_OPCODE(self, t):
		r'([A-Z]+(?![0-9]+))(?!([a-zA-Z0-9_]+))'
		# List of reserved words
		reserved = ['\bEQU\b', '\bORG\b', '\bEND\b', '\bADDS\b', '\bSUBS\b', '\bMULS\b', 
				'\bANDS\b', '\bORRS\b', '\bEORS\b', '\bBICS\b', '\bASRS\b', '\bLSLS\b', 
				'\bLSRS\b', '\bRORS\b', '\bCMN\b', '\bCMP\b', '\bMOVS\b', '\bBEQ\b', 
				'\bBNE\b', '\bBLT\b', '\bBL\b', '\bBX\b', '\bLDR\b', '\bSTR\b', '\bNOP\b']
		if t.value in reserved:
			t.type = t.value
		return t

	def t_newline(self, t):
		r'\n+'
		t.lexer.lineo += len(t.value)

	def t_error(self, t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

	# Ignored characters
	t_ignore = '\t+| +|\#[a-zA-Z0-9_]*'

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