"""
Expression_Recognizer.12.py
Read a simple expression from the user and parse it.
Allow use of named variables.

<expression>  ::=  <term> { ('+'|'-') <term> }*
<term>        ::=  <factor> { ('*'|'/'|'**'|'%') <factor> }*
<factor>      ::=  '(' <expression> ')' | ['+'|'-'] ( <integer> | <float> )
"""

import string
from tokenizer_12 import tokenizer, Token, SyntaxError

# get string of allowed alphabetic characters
Alphabetic = string.ascii_lowercase + string.ascii_uppercase

# define the environment dictionary
Environment = {}


class EvaluationError(Exception):
    """Exception raised when there's a problem evaluating the expression."""

    pass

def get_next_token(t_list):
    """A generator to return tokens one at a time.

    t_list  the list to yield token-by-token

    Returns None when the input list is exhausted.
    """

    # while we can, yield next char
    while t_list:
        yield t_list.pop(0)

    # else yield None
    yield None

def get_expression():
    """Recognize the EBNF rule for an <expression>:

        <expression> ::= <term> { ('+'|'-') <term> }*
    """

    global next_tok

    result = get_term()
    while (next_tok
            and next_tok.type == Token.token_operator
            and next_tok.value in '+-'):
        op = next_tok.value
        next_tok = next(tok_stream)
        term = get_term()
        if op == '+':
            result += term
        else:
            result -= term

    # a close parenthesis terminates the expression
    if (next_tok
            and next_tok.type == Token.token_operator
            and next_tok.value == ')'):
        # if there are no pending parentheses, error
        if nesting == 0:
            raise(EvaluationError(f"Unexpected ')'"))
        return result

    # otherwise check that we have finished the input token stream
    if next_tok is not None:
        raise(EvaluationError(f'Extra data after expression, next token is {next_tok}'))

    return result

def get_term():
    """Recognize the EBNF rule for a <term>:

        <term> ::= <factor> { ('*'|'/'|'**'|'%') <factor> }*
    """

    global next_tok

    result = get_factor()
    while (next_tok
            and next_tok.type == Token.token_operator
            and next_tok.value in ['*', '/', '**', '%']):
        op = next_tok.value
        next_tok = next(tok_stream)
        factor = get_factor()
        if op == '*':
            result *= factor
        elif op == '/':
            result /= factor
        elif op == '**':
            result = result ** factor
        elif op == '%':
            result %= factor
    return result

def get_factor():
    """Recognize the EBNF for a <factor>:

        <factor> ::= '(' <expression> ')' | ['+'|'-'] ( <integer> | <float> )
    """

    global next_tok, nesting

    if (next_tok is None
         or next_tok.type not in [Token.token_operator,
                                  Token.token_integer, Token.token_float]):
        raise EvaluationError(f'Expected integer or float, but got {next_tok}')

    # check for parenthesised expression
    if next_tok.type == Token.token_operator and next_tok.value == '(':
        nesting += 1
        next_tok = next(tok_stream)
        result = get_expression()
        if (next_tok is None
                or next_tok.type != Token.token_operator
                or next_tok.value != ')'):
            raise EvaluationError(f'Expected a close parenthesis, but got {next_tok}')
        nesting -= 1
        next_tok = next(tok_stream)
    else:
        # handle a leading operator
        negative = False        # assume a leading '+'
        if next_tok.type == Token.token_operator:
            if next_tok.value not in '+-':
                raise EvaluationError(f"Expected leading '+' or '-', but got {next_tok}")
            negative = (next_tok.value == '-')
            next_tok = next(tok_stream)

        # get the actual number value
        result = next_tok.value
        if negative:
            result = -result
        next_tok = next(tok_stream)

    return result

def dump_environment(args):
    """Dump the environment.

    args  list of variable names to dump

    If 'args' is None, list all Environment variables.
    """

    if args:
        max_name_len = 0
        for name in args:
            max_name_len = max(max_name_len, len(name))

        for name in args:
            if name in Environment:
                print('%-*s%f' % (max_name_len + 3, name, Environment[name]))
            else:
                print('%-*s%s' % (max_name_len + 3, name, 'UNDEFINED'))
    else:
        max_name_len = 0
        for name in Environment:
            max_name_len = max(max_name_len, len(name))

        for name in Environment:
            print('%-*s%f' % (max_name_len + 3, name, Environment[name]))

def handle_command(cmd_str):
    """Handle the command in the "cmd_str" string."""

    # get initial command word and following args, if any
    cmd_args = cmd_str.strip().split()
    print(f"cmd_args={cmd_args}")

    # perform the command
    cmd = cmd_args[0]
    args = None
    if len(cmd_args) > 0:
        args = cmd_args[1:]

    if cmd == '@var':
        dump_environment(args)
    else:
        print(f"Unrecognized command, got '{cmd}'")

def handle_assignment(assign_str):
    """Handle the command in the "cmd_str" string."""

    global next_tok, tok_stream, nesting

    # now check that first two tokens are <name> and "="
    assign_split = assign_str.split('=')
    if len(assign_split) != 2:
        # no '=', bad assignment
        print("Bad assignment, should be: <name> '=' <expression>")
        return None

    # split string into name and expression parts
    (name, expression) = assign_split
    print(f"name='{name}', expression='{expression}'")

    # check name string is just a single name
    name = name.strip()
    if len(name.split()) != 1:
        # bad name
        print(f"Bad assignment, <name> should be a single word, got '{name}'")

    # prepare the token stream for parsing
    try:
        token_list = tokenizer(expression)
    except SyntaxError as e:
        print(e)
        return None

    tok_stream = get_next_token(token_list)
    next_tok = next(tok_stream)
    nesting = 0     # number of open parentheses pending

    # evaluate the expression
    try:
        result = get_expression()
    except EvaluationError as e:
        print(e)
        return None

    # save the value in the Environment
    Environment[name] = result

def handle_expression(exp_str):
    """Parse an expression in "exp_str" string."""

    global next_tok, tok_stream, nesting

    # prepare the token stream for parsing
    try:
        token_list = tokenizer(exp_str)
    except SyntaxError as e:
        print(e)
        return None
    tok_stream = get_next_token(token_list)
    next_tok = next(tok_stream)
    nesting = 0     # number of open parentheses pending

    try:
        result = get_expression()
    except EvaluationError as e:
        print(e)
        return None

    return result

######
# Evaluate user expressions, handle commands, etc
######

while True:
    exp_str = input('Enter expression: ')
    if not exp_str:
        # nothing entered, quit
        break

    # check for commands or assignments before parsing
    exp_str = exp_str.strip()   # remove leading/trailing spaces
    if exp_str[0] == '@':
        handle_command(exp_str)
    elif exp_str[0] in Alphabetic:
        handle_assignment(exp_str)
    else:
        result = handle_expression(exp_str)
        if result:
            print(f'result = {result}')
