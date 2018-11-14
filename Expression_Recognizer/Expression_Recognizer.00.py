"""
Read a simple expression from sys.argv and print the result.

Usage: Expression_Recognizer.00.py <integer> <operator> <integer>
"""

import sys

args = sys.argv[1:]
integer1 = int(args[0])
operator = args[1]
integer2 = int(args[2])

if operator == '+':
    result = integer1 + integer2
elif operator == '-':
    result = integer1 - integer2

print(f'Expression {integer1} {operator} {integer2} = {result}')
