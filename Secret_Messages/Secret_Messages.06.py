"""
Secret_Messages.06.py

Decode a secret message given the original and encoded image files.

Usage: Secret_Messages.06.py <original image file> <encoded image file> <number of bits>
"""

import sys
from PIL import Image

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
        accum = accum + (bits << shift)    # shift bit value left
        shift += num_bits         # shift next value "num_bits" places
        if shift >= 8:            # if we have accumulated 8 bits
            if accum == 0:        # a zero byte, quit
                break
            result += chr(accum)  # put new character into result
            accum = 0             # initialize ready for next character
            shift = 0

    return result

def main(original_filename, encoded_filename, num_bits):
    # open input original_filename and get pixel data
    original_image = Image.open(original_filename)
    original_pixels = list(original_image.getdata())
    
    # ditto for the encoded file
    encoded_image = Image.open(encoded_filename)
    encoded_pixels = list(encoded_image.getdata())
    
    # get list of decoded Nbit values
    nbit_values = []
    for (o_pix, e_pix) in zip(original_pixels, encoded_pixels):
        # unpack each pixel tuple
        (o_r, o_g, o_b) = o_pix
        (e_r, e_g, e_b) = e_pix
    
        # decode the three pixel values, append to Nbit value list
        nbit_values.append(o_r ^ e_r)
        nbit_values.append(o_g ^ e_g)
        nbit_values.append(o_b ^ e_b)

    return nbits_to_string(nbit_values, num_bits)

# get the original and encoded filenames
if len(sys.argv) != 4:
    print(f'Sorry, expected a number of bits and two filenames')
    sys.exit(1)

original_filename = sys.argv[1]
encoded_filename = sys.argv[2]
num_bits = int(sys.argv[3])

print(f'original_filename={original_filename}, encoded_filename={encoded_filename}, num_bits={num_bits}')

result = main(original_filename, encoded_filename, num_bits)
print(result)
