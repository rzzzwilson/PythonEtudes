"""
Expression_Recognizer.11.py
Read a simple expression from the user and tokenize it.
Allow use of named variables.

<expression>   ::= <term> { ('+'|'-') <term> }*
<term>         ::= <factor> { ('*'|'/'|'**'|'%') <factor> }*
<factor>       ::= <variable> | '(' <expression> ')' | ['+'|'-'] ( <integer> | <float> )
<variable>     ::= <alphabetic> { ( '_' | <alphanumeric> ) }*
<alphabetic>   ::= 'a'|'A' ... 'z'|'Z'
<numeric>      ::= '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'|
<alphanumeric> ::= <alphabetic> | <numeric> | '_'
"""

from tokenizer_11 import tokenizer, Token, SyntaxError

# define the environmenr dictionary
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
        raise(EvaluationError(f'Unexpected end of expression, next token is {next_tok}'))

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

        <factor> ::= <name> [ '=' <expression> ] | '(' <expression> ')' | ['+'|'-'] ( <integer> | <float> )
    """

    global next_tok, nesting

    if (next_tok is None
         or next_tok.type not in [Token.token_name, Token.token_operator,
                                  Token.token_integer, Token.token_float]):
        raise EvaluationError(f'Expected integer or float, but got {next_tok}')

    # check for a name first
    if next_tok.type == Token.token_name:
        # found a name, check if it's followed by a '=' operator
        name = next_tok.value
        next_tok = next(tok_stream)
        if (next_tok
                and next_tok.type == Token.token_operator
                and next_tok.value == '='):
            # we have an assignment statement, get value of following <expression>
            next_tok = next(tok_stream)
            value = get_expression()
            # we MUST have an end to the input stream here
            if next_tok is not None:
                raise EvaluationError(f'Extra data after assignment statement: {next_tok}')
            # define the variable in the environment
            Environment[name] = value
            value = None        # assignment returns None
        else:
            # OK, just a named value, get the numeric value and return it
            try:
                value = Environment[name]
            except KeyError:
                raise EvaluationError(f'Undefined name: {name}')
        return value
    # maybe it's a parenthesized expression?
    elif next_tok.type == Token.token_operator and next_tok.value == '(':
        nesting += 1
        next_tok = next(tok_stream)
        result = get_expression()
        if (next_tok is None
                or next_tok.type != Token.token_operator
                or next_tok.value != ')'):
            raise EvaluationError(f'Expected a close parenthesis, but got {next_tok}')
        nesting -= 1
        next_tok = next(tok_stream)
    # nope, maybe a numeric value
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

# test the parser
while True:
    exp_str = input('Enter expression: ')
    if not exp_str:
        # nothing entered, quit
        break

    # prepare the token stream
    try:
        token_list = tokenizer(exp_str)
    except SyntaxError as e:
        print(e)
        continue
    tok_stream = get_next_token(token_list)
    next_tok = next(tok_stream)
    nesting = 0     # number of open parentheses pending

    try:
        result = get_expression()
    except EvaluationError as e:
        print(e)
        continue

    print(f'result = {result}')
