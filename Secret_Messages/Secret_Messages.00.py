"""
Secret_Messages.00.py

Get pixel data from an image file.

Usage: Secret_Messages.00.py <input file> <output file>
"""

import sys
from PIL import Image

# get the input and output filenames
if len(sys.argv) != 3:
    print(f'Sorry, expected two filenames')
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# open input input_filename and get pixel data
image = Image.open(input_filename)
pixels = list(image.getdata())
print(f'pixels={pixels}')

# change the pixel data and write it to the output file
pixels = [(0, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 0)]
print(f'NEW pixels={pixels}')
image.putdata(pixels)
image.save(output_filename)
