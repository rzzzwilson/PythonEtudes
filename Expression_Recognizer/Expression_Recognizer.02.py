"""
Read a simple expression from sys.argv and print the result.
Handle a range of errors.

Usage: Expression_Recognizer.02.py <integer> <operator> <integer>
"""

import sys

def error(msg):
    """Print an error message and terminate the program."""

    print(msg)
    sys.exit(1)

args = sys.argv[1:]
if len(args) != 3:
    error('You must supply three parameters: <integer> <operator> <integer>')

try:
    integer1 = int(args[0])
except ValueError:
    error('You must supply three parameters: <integer> <operator> <integer>')

operator = args[1]

try:
    integer2 = int(args[2])
except ValueError:
    error('You must supply three parameters: <integer> <operator> <integer>')

if operator == '+':
    result = integer1 + integer2
elif operator == '-':
    result = integer1 - integer2
else:
    error(f"Sorry, operator '{operator}' isn't valid, must be only '+' or '-'")

print(f'Expression {integer1} {operator} {integer2} = {result}')
