"""
Expression_Recognizer.08.py
Read a simple expression from the user and tokenize it.
"""

from tokenizer_08 import tokenizer, Token

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

        <expression> ::= <term> { (+|-) <term> }*
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
    return result

def get_term():
    """Recognize the EBNF rule for a <term>:

        <term> ::= <factor> { (*|/|**|%) <factor> }*
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

        <factor> ::= <integer> | <float>
    """

    global next_tok

    if (next_tok is None
         or next_tok.type not in [Token.token_integer, Token.token_float]):
        raise RuntimeError(f'Expected integer or float, but got {next_tok}')
    result = next_tok.value
    next_tok = next(tok_stream)
    return result

# test the parser
while True:
    exp_str = input('Enter expression: ')
    if not exp_str:
        # nothing entered, quit
        break

    # prepare the token stream
    token_list = tokenizer(exp_str)
    tok_stream = get_next_token(token_list)
    next_tok = next(tok_stream)

    result = get_expression()

    print(f'result = {result}')
