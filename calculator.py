# integral calculator using sympy expressions
from PyDesmos import Graph, to_latex
from sympy import sympify, SympifyError
import webbrowser
import os

function = input("Enter a function: ")
boundStart = int(input("Enter your starting bound: "))
boundEnd = int(input("Enter where your bound ends: "))


try:
    with Graph('my_graph') as G:
        G("f(x) = " + to_latex(sympify(function)))
        G("\\int_{a}^{b}" + "f(x)dx")  # integral
        G(a=boundStart)  # variable a at boundStart
        G(b=boundEnd)  # variable b at boundEnd
        # shades in bounded region
        G(r"0\le y\le f\left(x\right)\left\{a<x<b\right\}")
        G(r"0\ge y\ge f\left(x\right)\left\{a<x<b\right\}")
except SympifyError:
    print(f'Function in incorrect format. ex: (6/x^3) - (2*x)')

webbrowser.open(f'file://{os.path.realpath('my_graph.html')}')
