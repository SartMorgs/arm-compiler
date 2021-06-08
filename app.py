from armcompiler.compiler.ArmCompiler import *

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
	return ''

@app.route('/code', methods=['POST'])
def code():
	armcompiler = ArmCompiler('')
	armcompiler.build()

@app.route('/binary', methods=['GET'])
def get_binary():
	return 'Get Binary!'
