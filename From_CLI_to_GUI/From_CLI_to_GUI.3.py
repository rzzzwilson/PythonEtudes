"""
Prompt the user for two integer numbers and print the sum.
"""

def get_integer(prompt):
    """Prompt the user and return only an integer value."""

    while True:
        try:
            int_value = input(prompt)
            int_value = int(int_value)
            return int_value
        except ValueError:
            print(f'Sorry, only want integers.  Something like 123.')

int1 = get_integer('Enter the first integer: ')
int2 = get_integer('Enter the second integer: ')
the_sum = int1 + int2
print(f'The sum of {int1} and {int2} is {the_sum}')
