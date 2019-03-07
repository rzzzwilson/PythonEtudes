"""
Secret_Messages.07.1.py

Decode a secret message given the original and encoded image files.

Usage: Secret_Messages.07.1.py <original image file> <encoded image file> <number of bits>
"""

import sys
from PIL import Image

def nbits_to_string(data, num_bits):
    """Convert a list of Nbit values to a python bytestring.

    data      the list of Nbit values
    num_bits  the number of bits in each value in "data"

    Returns a simple python string.
    """

    result = []

    accum = 0                     # initialize state variables
    shift = 0

    for bits in data:
        accum = accum + (bits << shift)    # shift bit value left
        shift += num_bits         # shift next value "num_bits" places
        if shift >= 8:            # if we have accumulated 8 bits
            if accum == 0:        # a zero byte, quit
                break
            result.append(accum)  # put new character into result list
            accum = 0             # initialize ready for next character
            shift = 0

    return bytes(result)

def main(original_filename, encoded_filename, num_bits):
    """Decode an image into text.

    original_filename  the original image filename
    encoded_filename   the encoded image filename
    num_bits           the number of bits in the encoding

    Returns the decoded string.
    """

    # open input original_filename and get pixel data
    original_image = Image.open(original_filename)
    original_pixels = list(original_image.getdata())
    
    # ditto for the encoded file
    encoded_image = Image.open(encoded_filename)
    encoded_pixels = list(encoded_image.getdata())
    
    # collect the list of Nbit values
    data = []
    for (o_pix, e_pix) in zip(original_pixels, encoded_pixels):
        (o_r, o_g, o_b) = o_pix
        (e_r, e_g, e_b) = e_pix

        # decode the three pixel values and save in "data" list
        data.append(o_r ^ e_r)
        data.append(o_g ^ e_g)
        data.append(o_b ^ e_b)

    # convert to a list of bytes
    result = nbits_to_string(data, num_bits)

    # return a string
    return result.decode(encoding='utf_8')


# get the original and encoded filenames
if len(sys.argv) != 4:
    print(f'Sorry, expected two filenames and number of bits')
    sys.exit(1)

original_filename = sys.argv[1]
encoded_filename = sys.argv[2]
num_bits = int(sys.argv[3])

print(f'original_filename={original_filename}, encoded_filename={encoded_filename}')
print(f'num_bits={num_bits}')

result = main(original_filename, encoded_filename, num_bits)
print(result)

