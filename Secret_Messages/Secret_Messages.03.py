"""
Secret_Messages.03.py

Encode text characters into an image file.

Usage: Secret_Messages.03.py <input file> <output file> <text message>
"""

import sys
from PIL import Image

# global variables to support "nbit" functions
nbit_data = None
nbit_ch_index = None
nbit_char = None
nbit_index = None
nbit_num_bits = None
nbit_mask = None

def nbits_init(data, num_bits):
    """Initialize the "bit field" routines.

    data      the string of data to form into bit values
    num_bits  the number of bits to return each time
              (must be a power of 2, ie, 1, 2, 4, or 8)
    """

    global bit_data, bit_ch_index, bit_char, bit_index, bit_num_bits, bit_mask

    bit_data = str(data)        # the string to process
    bit_ch_index = 0            # index in string of next character
    bit_char = ord(bit_data[0]) # the current character (as integer)
    bit_index = 8               # index (from right) of next bit field (force next ch)
    bit_num_bits = num_bits     # the number of bits to return
    bit_mask = 2**num_bits - 1  # bit mask for rightmost N bits

def nbits_get():
    """Get the next N bits from the user data string.

    Returns the next N bit field, or None if no data left.
    """

    global bit_ch_index, bit_char, bit_index


    # move to next character if we need to
    if bit_index >= 8:
        if bit_ch_index >= len(bit_data):       # if end of text
            return None                         #   return None
        bit_char = ord(bit_data[bit_ch_index])  # else move to next character
        bit_ch_index += 1
        bit_index = 0

    # return next N bits
    result = bit_char & bit_mask                # get low N bits from variable
    bit_char = bit_char >> bit_num_bits         # shift variable to remove bits we are returning
    bit_index += bit_num_bits                   # bump the bit counter
    return result                               # return the result N bits

def main(input_filename, output_filename, text):
    """Encode a text message in an image file.

    input_filename   the name of the input image file
    output_filename  the name of the encoded putput image file
    text             the text message to encode

    The text data is encoded 2 bits at a time into each of the three pixel
    colour values.
    """

    # open input input_filename and get pixel data
    image = Image.open(input_filename)
    (image_width, image_height) = image.size
    num_pixels = image_width * image_height
    max_chars_in_image = num_pixels * 3 * 2 // 8
    pixels = list(image.getdata())

    # ensure the text message isn't too long to be encoded in the image file
    num_chars = len(text)           # assume 8-bit characters only in string
    if max_chars_in_image < num_chars:
        print(f'Sorry, the image can only contain {max_chars_in_image} characters')
        sys.exit(1)

    # prepare the text message "N bits at a time" software
    nbits_init(text, 2)

    # encode each N bits into the image pixel values
    new_pixels = []
    for pix in pixels:
        # get pixel colour values, handle a fourth value
        if len(pix) == 3:
            (r, g, b) = pix
            a = 255
        if len(pix) == 4:
            (r, g, b, a) = pix

        nbits = nbits_get()     # get N bits
        if nbits is None:       # if None
            nbits = 0           #     encode a 0 value (no change on XOR)
        xor_r = r ^ nbits

        nbits = nbits_get()
        if nbits is None:
            nbits = 0
        xor_g = g ^ nbits

        nbits = nbits_get()
        if nbits is None:
            nbits = 0
        xor_b = b ^ nbits

        new_pixels.append((xor_r, xor_g, xor_b, a))    # need to append a tuple

    # update the image and write a new file
    image.putdata(new_pixels)
    image.save(output_filename)


# get the input and output filenames and the text message
if len(sys.argv) != 4:
    print(f'Sorry, expected two filenames and a text message')
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]
text_msg = sys.argv[3]

print(f'input_filename={input_filename}, output_filename={output_filename}, text_msg={text_msg}')

main(input_filename, output_filename, text_msg)

