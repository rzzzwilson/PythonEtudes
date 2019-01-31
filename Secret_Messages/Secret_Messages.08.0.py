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

    # encode each N bits into the image pixel values
    new_pixels_list = []
    new_pix = []
    for (pix, nbits) in zip(image_pix, data_bits):
        new_pix.append(pix ^ nbits)
        if len(new_pix) == NumPixelColourValues:
            new_pixels_list.append(tuple(new_pix))    # need to append a tuple

    # update the image and write a new file
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

