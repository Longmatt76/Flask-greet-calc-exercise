# Put your app in here.

from flask import Flask, request

from operations import *

app = Flask(__name__)


"""returns a+b"""

@app.route('/add')
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return f"<h2>a + b = {result}</h2>"


"""returns a-b"""

@app.route('/sub')
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return f"<h2>a - b = {result}</h2>"


"""returns a*b"""

@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return f"<h2>a * b = {result}</h2>"


"""returns a/b"""

@app.route('/div')
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return f"<h2>a / b = {result}</h2>"


"""dict of the do math functions"""

math_funcs = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


""" function that puts all the others together into a single route view function"""

@app.route('/math/<math_func>')
def do_math(math_func):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = math_funcs[math_func](a, b)
    return f"<h2>{result}</h2>"
