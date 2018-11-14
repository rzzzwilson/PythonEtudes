"""
Read a simple expression from sys.argv and print the result.
Handle a range of errors.

Usage: Expression_Recognizer.01.py <integer> <operator> <integer>
"""

import sys

args = sys.argv[1:]
if len(args) != 3:
    print('You must supply three parameters: <integer> <operator> <integer>')
    sys.exit(1)

try:
    integer1 = int(args[0])
except ValueError:
    print('You must supply three parameters: <integer> <operator> <integer>')
    sys.exit(1)

operator = args[1]

try:
    integer2 = int(args[2])
except ValueError:
    print('You must supply three parameters: <integer> <operator> <integer>')
    sys.exit(1)

if operator == '+':
    result = integer1 + integer2
elif operator == '-':
    result = integer1 - integer2
else:
    print(f"Sorry, operator '{operator}' isn't valid, must be only '+' or '-'")
    sys.exit(1)

print(f'Expression {integer1} {operator} {integer2} = {result}')
