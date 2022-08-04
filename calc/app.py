from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def a():
  a = int(request.args['a'])
  b = int(request.args['b'])

  return f"{add(a, b)}"

@app.route('/sub')
def s():
  a = int(request.args['a'])
  b = int(request.args['b'])

  return f"{sub(a, b)}"

@app.route('/mult')
def m():
  a = int(request.args['a'])
  b = int(request.args['b'])

  return  f"{mult(a, b)}"

@app.route('/div')
def d():
  a = int(request.args['a'])
  b = int(request.args['b'])

  return f"{div(a, b)}"