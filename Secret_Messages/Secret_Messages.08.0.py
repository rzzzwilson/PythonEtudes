"""
Secret_Messages.08.py

Encode unicode text characters into an image file.
This version uses iterators for text and image data.

Usage: Secret_Messages.08.py <input file> <output file> <text message or file>
"""

import sys
from PIL import Image
import data_bitstream
import image_iterator

# default values
BitsPerPixelColour = 2      # 2 bits per colour value
NumPixelColourValues = 4    # using 4 pixel values, RGBA
BitsPerColour = 8           # 8 bits per colour value


def stream_integer(int_value, num_bits):
    """Stream a 4 byte integer value as 'num_bits' bit values."""

    mask = 2**num_bits - 1         # bit mask for rightmost N bits

    for _ in range(32 // num_bits):
        result = int_value & mask  # get low N bits from variable
        int_value >>= num_bits     # shift variable to remove bits we are returning
        yield result               # return the result N bits

def main(input_filename, output_filename, text):
    """Encode a text message in an image file.

    input_filename   the name of the input image file
    output_filename  the name of the encoded putput image file
    text             the text message to encode

    The text data is encoded 'BitsPerPixelColour' bits at a time into each of
    the pixel colour values.
    """

    # open input input_filename and get pixel data
    image = Image.open(input_filename)
    (image_width, image_height) = image.size
    num_pixels = image_width * image_height
    max_chars_in_image = num_pixels * NumPixelColourValues * BitsPerPixelColour // BitsPerColour
    pixels = list(image.getdata())

    # convert the text message in unicode to a sequence of bytes
    text = bytes(text, 'utf-8')

    # ensure the text message isn't too long to be encoded in the image file
    num_chars = len(text)
    if max_chars_in_image < num_chars:
        print(f'Sorry, the image can only contain {max_chars_in_image} characters')
        sys.exit(1)

    # calculate the number of complete pixels we will use in the image
    # num_chars / (bits_per_pixel_colour // number_of_pixel_colours // bits_encoded_per_pixel_colour)
    num_pixels = num_chars * (BitsPerColour // NumPixelColourValues // BitsPerPixelColour)

    # prepare the text message "N bits at a time" stream
    data_bits = data_bitstream.stream(text, BitsPerPixelColour)

    print(f'num_chars={num_chars}, num_pixels={num_pixels}')

    # prepare the image pixel value iterator
    image_pix = image_iterator.image_iterator(image, num_pixels)

    # encode the number of chars as a 4 byte integer value, N bits at a time
    num_count_values = 32 // BitsPerPixelColour
    num_mask = 2**BitsPerPixelColour - 1

    # encode the number of text characters into the image
    new_pixels_list = []
    new_pix = []
    int_stream = stream_integer(num_chars, BitsPerPixelColour)
    for (pix, int_val) in zip(image_pix, int_stream):
        print(f'int loop: pix={pix}, int_val={int_val}')
        new_pix.append(pix ^ int_val)
        if len(new_pix) == NumPixelColourValues:
            new_pixels_list.append(tuple(new_pix))
            new_pix = []
    print(f'after integer, new_pixels_list={new_pixels_list}')
    new_pix = []

    # encode each message N bits into the image pixel values
    for (pix, nbits) in zip(image_pix, data_bits):
        print(f'data loop: pix={pix}, nbits={nbits}')
        new_pix.append(pix ^ nbits)
        if len(new_pix) == NumPixelColourValues:
            new_pixels_list.append(tuple(new_pix))    # need to append a tuple
            new_pix = []

    # update the image and write a new file
    print(f'new_pixels_list={new_pixels_list}')
    image.putdata(new_pixels_list)
    image.save(output_filename)


# get the input and output filenames and the text message
if len(sys.argv) != 4:
    print(f'Sorry, expected two filenames and a text message')
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]
text_msg = sys.argv[3]

# maybe 'text_msg' is actually a filename
# try to open the file - if that works read the file contents
# if there is no file then 'text_msg' contains the text to encode
try:
    with open(text_msg) as fd:
        text_msg = fd.read()
except FileNotFoundError:
    pass

print(f'input_filename={input_filename}, output_filename={output_filename}')
print(f'text_msg:\n{text_msg}')

# call the encode routine
main(input_filename, output_filename, text_msg)

