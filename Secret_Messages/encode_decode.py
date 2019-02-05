"""
Functions to encode/decode a string.

encode(data, num_bits)
    Converts a string into a stream of N bit integers consisting of:
    o 8 1 bit values encoding the number of bits in the following encoding
    o N bit values encoding a 2 byte integer holding the number of bytes encoded
    o N bit values holding encoded data

decode(data)
    Decoding returns the original encoded string.

Handles Unicode characters.
"""

def encode(data, num_bits):
    """Encode the given string as a stream of integer values.

    data      the string to stream as N bits at a time
    num_bits  the number of bits to stream (1, 2, 4 or 8)

    Yields N bit values that encode the given string.

    The first 8 1bit values are the number of bits in the following encoding.
    The next 2*8/num_bits Nbit values are the number of characters in the byte string.
    The final Nbit values are the original data string, in bytestring format, num_bits at a time.
    """

    # we will actually send the bytestring form of the string
    # this makes handling of unicode easier
    byte_data = bytes(data, 'utf-8')

    # we first stream the number of bits the following encoding uses
    # send a 1 byte integer value as 1 bit values
    i_data = num_bits
    for _ in range(8):
        yield i_data & 0b1
        i_data >>= 1

    # now stream number of bytes in the 'byte_data' bytestring
    # send this as an integer of 2 bytes, 'num_bits' at a time
    num_bytes = len(byte_data)
    mask = 2**num_bits - 1          # get rightmost N bits turned on
    for _ in range(2*8//num_bits):
        yield num_bytes & mask
        num_bytes >>= num_bits

    # now stream the entire bytestring of data
    for ch in byte_data:
        for _ in range(8 // num_bits):
            yield ch & mask
            ch >>= num_bits

def decode(data):
    """Decode a sequence of values that were encoded by 'encode()'.

    data  the list of values to decode
    """

    # first, accumulate the first 8 values as 1 bit values (ie, num_bits)
    num_bits = 0
    shift = 0
    for _ in range(8):
        v = next(data)
        num_bits |= (v & 0b1) << shift
        shift += 1

    # now we get the byte count from the next 2*8/num_bits values (ie, num_bytes)
    num_bytes = 0
    mask = 2**num_bits - 1
    shift = 0
    for _ in range(2*8//num_bits):
        v = next(data)
        num_bytes |= (v & mask) << shift
        shift += num_bits

    # now collect the remaining values into a bytestring
    byte_values = []
    byte_value = 0
    shift = 0
    for v in data:
        byte_value |= (v & mask) << shift
        shift += num_bits
        if shift >= 8:
            byte_values.append(byte_value)
            byte_value = 0
            shift = 0

    # now convert the list of byte values to a "unicode" string
    return bytes(byte_values).decode(encoding='utf_8')


if __name__ == '__main__':
    import sys

    # get test text and number of bits to return
    if len(sys.argv) != 3:
        print('Usage: xyzzy.py <number of bits> <text message>')
        sys.exit(1)
    number_of_bits = int(sys.argv[1])
    data = sys.argv[2]

    print(f"  data='{data}'")
    encoded_data = encode(data, number_of_bits)
    result = decode(encoded_data)
    print(f"result='{result}'")

