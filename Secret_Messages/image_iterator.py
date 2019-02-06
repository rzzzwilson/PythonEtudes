"""
image_iterator.py

Create an iterator that iterates through the pixels of an image returning
individual red, green and blue pixel values.

Cannot handle images with a transparency band.

Usage: image_iterator.py <image file>
"""

from PIL import Image

def image_iterator(image, num_pixels=None):
    """Create an iterator for a number of pixels of an image.

    image       the open Pillow image object
    num_pixels  the number of pixels to iterate over
                (if None, use all pixels values in the image)
    """

    count = 0
    if num_pixels is None:
        (image_width, image_height) = image.size
        num_pixels = image_width * image_height

    for pix in image.getdata():
#        # get pixel colour values, assume a missing 'transparency' value is 255
#        try:
#            (r, g, b) = pix
#            a = 255
#        except ValueError:
#            (r, g, b, a) = pix

        (r, g, b) = pix

        yield r
        yield g
        yield b
#        yield a

        count += 1
        if count >= num_pixels:
            break

if __name__ == '__main__':
    import sys

    # get the input and output filenames and the text message
    if len(sys.argv) != 2:
        print('Usage: image_iterator.py <image file>')
        sys.exit(1)
    
    image_filename = sys.argv[1]
    new_filename = 'xyzzy.bmp'
    
    print(f'image_filename={image_filename}')
    
    # use the filename to get image_iterator and loop over it
    image = Image.open(image_filename)
    pixels = list(image.getdata())
    print(f'pixels={pixels}')
    #image = Image.open(image_filename)
    i_iterator = image_iterator(image, 2)
    new_pixels = []
    accum = []
    for p_value in i_iterator:
        print(f'value={p_value:x}')
        accum.append(p_value)
        if len(accum) >= 4:
            new_pixels.append(tuple(accum))
            accum = []
    print(f'new_pixels={new_pixels}')
    image.putdata(new_pixels)
    image.save(new_filename)
    
