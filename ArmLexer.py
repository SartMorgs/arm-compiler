# module: tokrules.py
# This module just contains the lexing rules

# The lex.py module is used to brak input text into a collection of tokens specified by a collection of regular expression rules.
# yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar

import ply.lex as lex
import re

class ArmLexer(object):
	# List of tokens names
	tokens = [
		'COMMA', 'SEMICOLON', 'REGISTER', 'FUNCTIONNAME',
		'ADDRESSNAME', 'NUMBER', 'COMMENTS', 'OPCODE'
		]

	# Regular expression rules for simples tokens
	#t_OPCODE = r'/(^ADDS(?=\s))|(^SUBS(?=\s))|(^LDR(?=\s))|(^STR(?=\s))|(^ORRS(?=\s))|(^ANDS(?=\s))/'
	t_COMMA = r'\,'
	t_SEMICOLON = r'\;'
	t_REGISTER = r'R[0-9]+'
	t_FUNCTIONNAME = r'((?!R[0-9]+)([a-zA-Z_]+[a-zA-Z0-9_]*))'
	t_ADDRESSNAME = r'[a-zA-Z_]+[a-zA-Z0-9_]*(?=\sEQU.)'
	t_NUMBER = r'[0-9]+'

	# A regular expression rule with some action code
	def t_OPCODE(self, t):
		r'[A-Z]+(?![0-9]+)\s'
		# List of reserved words
		reserved = ['EQU\s', 'ORG\s', 'END\s', 'ADDS\s', 'SUBS\s',
				'MULS\s', 'ANDS\s', 'ORRS\s', 'EORS\s', 'BICS\s', 'ASRS',
				'LSLS\s', 'LSRS\s', 'RORS\s', 'CMN\s', 'CMP\s',
				'MOVS\s',	'BEQ\s', 'BNE\s', 'BLT\s', 'BL\s',
				'BX\s', 'LDR\s', 'STR\s', 'NOP\s']
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
	t_ignore_COMMENTS = r'/(?:[#]).*/'
	t_ignore = '\t+| +'

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