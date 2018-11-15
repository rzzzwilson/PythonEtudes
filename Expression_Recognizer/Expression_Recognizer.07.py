"""
Expression_Recognizer.07.py
Read a simple expression from the user and tokenize it.
"""

import sys

class SyntaxError(Exception):
    """A syntax error exception raised by tokenizer()."""

    pass

class Token:
    """A class for simple Tokens."""

    # the types of Token
    (token_integer, token_float, token_operator) = range(3)

    def __init__(self, ttype, value):
        self.type = ttype
        self.value = value

def dump(msg, n_ch, s_l):
    print(f"{msg}, next_ch='{n_ch}', s_l={s_l}")

def tokenizer(s):
    """Tokenize the input string and return a list of tokens.

    s  the string to tokenize

    Returns a list of tokens, or raises SyntaxError.
    """

    token_list = []

    # turn the input string into a list for easy handling
    s_list = list(s)

    # keep the next character in "next_ch"
    try:
        next_ch = s_list.pop(0)
    except IndexError:
        # string is empty, return empty token list
        return token_list

    dump('before loop', next_ch, s_list)

    # now look at next token
    while next_ch is not None:
        dump('top of loop', next_ch, s_list)

        if next_ch in '+-*/':
            dump('possible operator', next_ch, s_list)
            # we have an operator
            t = Token(Token.token_operator, next_ch)

            # get next character, because we might have '**'
            try:
                next_ch = s_list.pop(0)
            except IndexError:
                # string is empty, return the token list
                break

            dump('possible **', next_ch, s_list)

            # check for '**'
            if next_ch == '*':
                # operator was '**', fix the token
                t.value = '**'

            # append the new toke to the result list
            token_list.append(t)

            # refresh next_ch
            try:
                next_ch = s_list.pop(0)
            except IndexError:
                # string is empty, return the token list
                break
        elif next_ch in '0123456789.':
            dump('possible integer or float', next_ch, s_list)
            # we have an integer or float value
            number = ''
            while next_ch in '0123456789.':
                number += next_ch

                # refresh next_ch
                try:
                    next_ch = s_list.pop(0)
                except IndexError:
                    # string is finished, set next_ch to None
                    next_ch = None

                dump(f'value loop, number={number}', next_ch, s_list)

            # have accumulated a number and next_ch has been refreshed
            # see if we have an integer, float or error
            ttype = Token.token_integer
            try:
                value = int(number)
            except ValueError:
                # no integer, try float
                ttype = Token.token_float
                try:
                    value = float(number)
                except ValueError:
                    # it's an error, raise SyntaxError
                    raise SyntaxError(f'unrecognized value: {number}')

            # we have an integer or float
            t = Token(ttype, value)
            token_list.append(t)
        elif next_ch == ' ':
            dump('ignoring space', next_ch, s_list)
            # we ignore spaces, but must refresh next_ch
            try:
                next_ch = s_list.pop(0)
            except IndexError:
                # string is empty, return the token list
                break
        else:
            dump('unrecognized character', next_ch, s_list)
            # unrecognized character
            raise SyntaxError(f"unrecognized character: '{next_ch}'")

    return token_list


expression = input('Enter expression: ')

token_list = tokenizer(expression)

print(f'token_list = {token_list}')
