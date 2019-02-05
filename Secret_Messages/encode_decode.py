"""
Functions to encode/decode a string.

encode(data, num_bits)
    Converts a string into a stream of N bit integers consisting of:
    o 8 1 bit values encoding the number of bits in the following encoding
    o N bit values holding encoded data

decode(data)
    Decoding returns the original encoded string.

encode_size(data, num_bits)
    Returns the total number of Nbit values that result from the encoding.

Handles Unicode characters.
"""

def encode_size(data, num_bits):
    """Returns the actual number of encoded values that would be used.

    data      the text message to encode (as a bytetring)
    num_bits  the number of bits to encode the message with
    """

    return 8 + len(data)*8//num_bits       # 8 bits in a byte


def encode(data, num_bits):
    """Encode the given string as a stream of integer values.

    data      the string to stream as N bits at a time
    num_bits  the number of bits to stream (1, 2, 4 or 8)

    Yields N bit values that encode the given string.

    The first 8 1bit values are the number of bits in the following encoding.
    The final Nbit values are the original data string, num_bits at a time.
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

    # now stream the entire bytestring of data
    mask = 2**num_bits - 1          # get rightmost N bits turned on
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

    # now collect the remaining values into a bytestring
    byte_values = []
    byte_value = 0
    mask = 2**num_bits - 1      # bitmask, rightmost 'num_bits' bits turned on
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

    if number_of_bits not in (1, 2, 4, 8):
        msg = f"Expected <number of bits> to be 1, 2, 4 or 8, got '{number_of_bits}'."
        raise ValueError(msg)

    print(f"  data='{data}'")
    encoded_data = encode(data, number_of_bits)
    result = decode(encoded_data)
    print(f"result='{result}'")

