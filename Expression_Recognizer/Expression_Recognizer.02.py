    """
    Expression_Recognizer.02.py
    Read a simple expression from the user and print the result.
    Check parameters for some errors using an error() function..
    
    Recognizes an expression of the form: <integer> <operator> <integer>
    where <operator> may be either '+' or '-'.
    """
    
    import sys
    
    def error(msg):
        """Print an error message and terminate."""
    
        print(msg)
        sys.exit(1)
    
    expression = input('Enter expression: ')
    fields = expression.split()
    
    try:
        (integer1, operator, integer2) = fields
    except ValueError:
        error(f"Expected an expression of three fields: <integer> <operator> <integer>\nGot: '{expression}'")
    
    try:
        integer1 = int(integer1)
    except ValueError:
        error(f"The first number must be an integer\nGot: '{integer1}'")
    
    try:
        integer2 = int(integer2)
    except ValueError:
        error(f"The second number must be an integer\nGot: '{integer1}'")
    
    if operator == '+':
        result = integer1 + integer2
    elif operator == '-':
        result = integer1 - integer2
    else:
        error(f"The operator must be '+' or '-', got '{operator}'")
    
    print(f'Expression {integer1} {operator} {integer2} = {result}')
