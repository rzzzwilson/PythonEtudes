"""
Expression_Recognizer.04.py
Read a simple expression from the user and print the result.
Check parameters for some errors using an error() function.

Recognizes an expression of the form: <float> <operator> <float>
where <operator> may be either '+', '-', '*' or '/'.
"""

import sys

def error(msg):
    """Print an error message and terminate."""

    print(msg)
    sys.exit(1)

expression = input('Enter expression: ')
fields = expression.split()

try:
    (float1, operator, float2) = fields
except ValueError:
    error(f"Expected an expression of three fields: <float> <operator> <float>\nGot: '{expression}'")

try:
    float1 = float(float1)
except ValueError:
    error(f"The first number must be an floating point number\nGot: '{float1}'")

try:
    float2 = float(float2)
except ValueError:
    error(f"The second number must be an floating point number\nGot: '{float1}'")

if operator == '+':
    result = float1 + float2
elif operator == '-':
    result = float1 - float2
elif operator == '*':
    result = float1 * float2
elif operator == '/':
    result = float1 / float2
else:
    error(f"The operator must be '+', '-', '*' or '/', got '{operator}'")

print(f'Expression {float1} {operator} {float2} = {result}')
