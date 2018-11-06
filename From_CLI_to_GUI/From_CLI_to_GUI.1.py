"""
Prompt the user for two integer numbers and print the sum.
"""

int1 = input('Enter the first integer: ')
int1 = int(int1)    # convert the input string to a number
int2 = input('Enter the second integer: ')
int2 = int(int2)
the_sum = int1 + int2
print(f'The sum of {int1} and {int2} is {the_sum}')
