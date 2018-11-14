"""
Expression_Recognizer.01.py
Read a simple expression from the user and print the result.
Check parameters for some errors.

Recognizes an expression of the form: <integer> <operator> <integer>
where <operator> may be either '+' or '-'.
"""

import sys

expression = input('Enter expression: ')
fields = expression.split()

try:
    (integer1, operator, integer2) = fields
except ValueError:
    print(f"Expected an expression of three fields: <integer> <operator> <integer>\nGot: '{expression}'")
    sys.exit(1)

try:
    integer1 = int(integer1)
except ValueError:
    print(f"The first number must be an integer\nGot: '{integer1}'")
    sys.exit(1)

try:
    integer2 = int(integer2)
except ValueError:
    print(f"The second number must be an integer\nGot: '{integer1}'")
    sys.exit(1)

if operator == '+':
    result = integer1 + integer2
elif operator == '-':
    result = integer1 - integer2
else:
    print(f"The operator must be '+' or '-', got '{operator}'")
    sys.exit(1)

print(f'Expression {integer1} {operator} {integer2} = {result}')
