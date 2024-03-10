# integral calculator using sympy expressions
from PyDesmos import Graph, to_latex
from sympy import sympify

function = input("Enter a function: ")
boundStart = int(input("Enter your starting bound: "))
boundEnd = int(input("Enter where your bound ends: "))

# constants throws an error when parsed, so we'll separate it
constant = ""
i = 0
while i < len(function) - 1 and function[i].isdigit():
    constant += function[i]
    i += 1

reduced_function = function[i:]

with Graph('my_graph') as G:
    G("f(x) = " + constant + to_latex(sympify(reduced_function)))
    G("\\int_{a}^{b}" + "f(x)dx")  # integral
    G(a=boundStart)  # variable a at boundStart
    G(b=boundEnd)  # variable b at boundEnd
    # shades in bounded region
    G(r"0\le y\le f\left(x\right)\left\{a<x<b\right\}")
    G(r"0\ge y\ge f\left(x\right)\left\{a<x<b\right\}")
