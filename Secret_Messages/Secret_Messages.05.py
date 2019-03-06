"""
Secret_Messages.05.py

Decode a list of N bit values into a text string.

Usage: Secret_Messages.05.py
"""

def nbits_to_string(data, num_bits):
    """Convert a list of Nbit values to a python string.

    data      the list of Nbit values
    num_bits  the number of bits in each value in "data"

    Returns a simple python string.
    """

    result = ''

    accum = 0                     # initialize state variables
    shift = 0

    for bits in data:
        accum += bits << shift    # shift bit value left
        shift += num_bits         # shift next value "num_bits" places
        if shift >= 8:            # if we have 8 bits
            result += chr(accum)  # put new character into result
            accum = 0             # initialize ready for next character
            shift = 0

    return result

# test code
data = [1, 2, 0, 1, 0, 1, 3, 1,    # the 2bit-encoded message
        0, 0, 2, 0, 3, 1, 3, 1,
        3, 3, 2, 1, 2, 0, 3, 1,
        3, 2, 2, 1, 3, 0, 3, 1,
        1, 0, 2, 0]

decoded_data = nbits_to_string(data, 2)
print(decoded_data)
