"""
Secret_Messages.01.py

Encode text characters into an image file.

Usage: Secret_Messages.01.py <input file> <output file> <text message>
"""

import sys
from PIL import Image

# get the input and output filenames and the text message
if len(sys.argv) != 4:
    print(f'Sorry, expected two filenames and a text message')
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]
text_msg = sys.argv[3]

print(f'input_filename={input_filename}, output_filename={output_filename}, text_msg={text_msg}')

# open input input_filename and get pixel data
image = Image.open(input_filename)
pixels = image.getdata()
print(f'pixels={list(pixels)}')

# encode each text character into the image pixel RED values
new_pixels = []
for (pix, ch) in zip(pixels, text_msg):
    (r, g, b) = pix
    xor_r = r ^ ord(ch)
    new_pixels.append((xor_r, g, b))    # need to append a 3-tuple
print(f'new_pixels={new_pixels}')

# update the image and write a new file
image.putdata(new_pixels)
image.save(output_filename)
