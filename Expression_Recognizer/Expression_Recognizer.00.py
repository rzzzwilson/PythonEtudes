"""
Read a simple expression from the user and print the result.

Recognizesan expression of the form: <integer> <operator> <integer>
where <operator> may be either '+' or '-'.
"""

expression = input('Enter expression: ')
fields = expression.split()

(integer1, operator, integer2) = fields

integer1 = int(integer1)
integer2 = int(integer2)

if operator == '+':
    result = integer1 + integer2
elif operator == '-':
    result = integer1 - integer2

print(f'Expression {integer1} {operator} {integer2} = {result}')
