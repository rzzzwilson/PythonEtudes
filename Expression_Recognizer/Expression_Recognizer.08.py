"""
Expression_Recognizer.08.py
Read a simple expression from the user and tokenize it.
"""

from tokenizer_08 import tokenizer

def eval_exp(s):
    """Evaluate the input string and return a value.

    s  the string to eval_exp

    Returns a numeric value.
    """

    # convert the inpus string to a list of tokens
    token_list = tokenizer(s)

    return token_list

# test the eval_exp() function
while True:
    exp_str = input('Enter expression: ')
    if not exp_str:
        # nothing entered, quit
        break
    result = eval_exp(exp_str)
    print(f'result = {result}')
