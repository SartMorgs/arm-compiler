import flask
import json

from flask import request
import armcompiler.app.compiler.ArmCompiler as cp 


# use https://www.freeformatter.com/json-escape.html#ad-output for format

app = flask.Flask(__name__)
app.config["DEBUG"] = True

compiler = cp.ArmCompiler()

@app.route('/', methods=['GET'])
def home():
	return "<h1>Arm Compiler API</h1><p>This site is a prototype API for arm cortex m0 compiler.</p>"

@app.route('/api/v1/code', methods=['POST'])
def build_code():
	data = request.get_json()
	compiler.set_multiline_code(data.get('code', ''))
	compiler.build()
	response = compiler.compilation()
	return response

@app.route('/api/v1/instruction', methods=['GET'])
def get_instruction_list():
	compiler.build_instruction_list_json()
	instruction_list = compiler.get_instruction_list_json()
	return instruction_list

@app.route('/api/v1/directive', methods=['GET'])
def get_directive_list():
	compiler.build_directive_list_json()
	directive_list = compiler.get_directive_list_json()
	return directive_list	

app.run()