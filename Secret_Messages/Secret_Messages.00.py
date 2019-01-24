"""
Secret_Messages.00.py

Get pixel data from an image file.

Usage: Secret_Messages.00.py <input file> <output file>
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
pixels = list(image.getdata())
print(f'pixels={pixels}')

# change the pixel data and write it to the output file
new_pixels = [(0, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 0)]
print(f'new_pixels={new_pixels}')

# save new pixel data into a new image file
image.putdata(new_pixels)
image.save(output_filename)
