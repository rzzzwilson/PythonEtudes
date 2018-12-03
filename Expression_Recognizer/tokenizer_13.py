"""
The tokenizer.13.py module.

Allow variable names.
"""

import string

# definitions of alphabetic and alphanumeric characters
Alphabetic = string.ascii_lowercase + string.ascii_uppercase
Alphanumeric = string.ascii_lowercase + string.ascii_uppercase + string.digits


class Token:
    """A class for simple Tokens."""

    # the types of Token
    (token_integer, token_float, token_operator, token_name) = range(4)

    # dictionary to convert a token number to a string
    tok_str = {token_integer: 'integer', token_float: 'float',
               token_operator: 'operator', token_name: 'name'}

    def __init__(self, ttype, value):
        self.type = ttype
        self.value = value

    def __repr__(self):
        return f"<{Token.tok_str[self.type]}: '{self.value}'>"

def get_next_char(s):
    """A generator to return chars one at a time.

    s  the string to yield char-by-char

    Returns None when the input string is exhausted. 
    """

    # make a list from the string - easier handling
    s_list = list(s)

    # while we can, yield next char
    while s_list:
        yield s_list.pop(0)

    # else yield None
    yield None

class SyntaxError(Exception):
    """A syntax error exception raised by tokenizer()."""

    pass

def tokenizer(s):
    """Tokenize the input string and return a list of tokens.

    s  the string to tokenize

    Returns a list of tokens, or raises SyntaxError.
    """

    # the token list we will return
    token_list = []

    # keep the next character in "next_ch"
    ch_stream = get_next_char(s)
    next_ch = next(ch_stream)
    if next_ch is None:
        # string is empty, return empty token list
        return token_list

    # now look at next token
    while next_ch is not None:
        if next_ch in '+-*/%()':
            # we have an operator, make token and append to result list
            t = Token(Token.token_operator, next_ch)
            token_list.append(t)

            # get next character
            next_ch = next(ch_stream)
            if next_ch is None:
                # end of string
                break

            # check for '**'
            if next_ch == '*':
                # operator was '**', fix the already appended token
                t.value = '**'      
                # refresh 'next_ch'
                next_ch = next(ch_stream)
                if next_ch is None:
                    break
        elif next_ch in '0123456789.':
            # we have an integer or float value
            number = ''
            while next_ch in '0123456789.':
                number += next_ch

                # refresh next_ch
                next_ch = next(ch_stream)
                if next_ch is None:
                    # end of input characters
                    break

            # have accumulated a number and next_ch has been refreshed
            # see if we have an integer, float or error
            ttype = Token.token_integer         # assume an integer
            try:
                value = int(number)
            except ValueError:
                # no integer, try float
                ttype = Token.token_float       # no, assume float
                try:
                    value = float(number)
                except ValueError:
                    # it's an error, raise SyntaxError
                    raise SyntaxError(f'unrecognized value: {number}')

            # we have an integer or float, create new token, append
            t = Token(ttype, value)
            token_list.append(t)
        elif next_ch == ' ':
            # we ignore spaces, but must refresh next_ch
            next_ch = next(ch_stream)
            if next_ch is None:
                break
        elif next_ch in Alphabetic:
            # start collecting a name token
            name = ''
            while next_ch in Alphanumeric + '_':
                name += next_ch
                next_ch = next(ch_stream)
                if next_ch is None:
                    break       # end of stream, so end of name
            t = Token(Token.token_name, name)
            token_list.append(t)
        else:
            # unrecognized character
            raise SyntaxError(f"unrecognized character: '{next_ch}'")

    return token_list

# simple little test harness for debug
if __name__ == '__main__':
    while True:
        exp_string = input('Enter expression: ')
        if not exp_string:
            break
        token_list = tokenizer(exp_string)
        print(token_list)
