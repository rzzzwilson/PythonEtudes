"""
image_iterator.py

Create an iterator that sequences through the pixels of an image returning
individual red, green and blue pixel values.

Cannot handle images with a fourth transparency band.

Usage: image_iterator.py <image file>
"""

def image_iterator(image):
    """Create an iterator for a number of pixels of an image.

    image       the open Pillow image object

    Returns a generator object containing the image pixel colour values.
    """

    for pix in image.getdata():
        (r, g, b) = pix

        yield r
        yield g
        yield b

if __name__ == '__main__':
    import sys
    from PIL import Image

    # get the input filename
    if len(sys.argv) != 2:
        print('Usage: image_iterator.py <image file>')
        sys.exit(1)
    
    image_filename = sys.argv[1]
    
    print(f'image_filename={image_filename}')
    
    # use the filename to get image_iterator and loop over it
    image = Image.open(image_filename)
    pixels = list(image.getdata())
    print(f'pixels={pixels}')
    print('values=', end='')
    for p_value in image_iterator(image):
        print(f'{p_value}, ', end='')
    print()
