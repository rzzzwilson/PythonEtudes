"""
Functions to encode/decode a string.

encode(data, num_bits)
    Converts a string into a stream of Nbit integers consisting of:
    o 4 1 bit values encoding the number of bits in the following encoding
    o Nbit values for a 2 byte integer that holds the number of encoded values
    o Nbit values holding encoded data

decode(data)
    Converts an encoded sequence as returnd by encode() to the originl string.

encode_size(data, num_bits)
    Returns the total number of Nbit values that result from encoding "data".

Handles Unicode characters.
"""

def encode_size(data, num_bits):
    """Returns the actual number of encoded values that would be used.

    data      the text message to encode (as a unicode string)
    num_bits  the number of bits to encode the message with

    Returns the number of values in the sequence that is returned by the
    encode() function.  We require this function because we can't get the
    length of data produced by a generator function without destroying
    the generator function state.
    """

    return 8 + 2*8//num_bits + len(bytes(data, 'utf-8'))*8//num_bits       # 8 bits in a byte


def encode(data, num_bits):
    """Encode the given string as a stream of integer values.

    data      the unicode string to stream as N bits at a time
    num_bits  the number of bits to stream (1, 2, 4 or 8)

    Yields N bit values that encode the given string.

    The first 4 1bit values are the number of bits in the following encoding.
    The final Nbit values are the original data string, num_bits at a time.
    """

    # we will actually send the bytestring form of the string
    # this makes handling of unicode easier
    bytes_data = bytes(data, 'utf-8')

    # we first stream the number of bits the following encoding uses
    # send a 1 byte integer value as 1 bit values
    i_data = num_bits
    for _ in range(4):
        yield i_data & 0b1
        i_data >>= 1

    # next we send a number of Nbit values that is a 2 byte integer
    # that is the number of encoded values following
    mask = 2**num_bits - 1          # bit mask with rightmost N bits turned on
    num_nbits = len(bytes_data) * 8//num_bits
    for _ in range(2 * 8 // num_bits):
        yield num_nbits & mask
        num_nbits >>= num_bits

    # now stream the entire bytestring of data
    for ch in bytes_data:
        for _ in range(8 // num_bits):
            yield ch & mask
            ch >>= num_bits


def decode(data):
    """Decode a sequence of values that were encoded by 'encode()'.

    data  the sequence of values to decode
    """

    # first, accumulate the first 4 values as 1 bit values (ie, num_bits)
    num_bits = 0
    shift = 0
    for _ in range(4):
        v = next(data)
        num_bits |= (v & 0b1) << shift
        shift += 1

    # next, get the number of bytes in the encoded data
    mask = 2**num_bits - 1      # bitmask, rightmost 'num_bits' bits turned on
    num_nbits = 0
    shift = 0
    for _ in range(2 * 8 // num_bits):
        v = next(data)
        num_nbits |= v << shift
        shift += num_bits

    # now collect the remaining values into a bytestring
    byte_values = []
    byte_value = 0
    shift = 0
    count = 0
    for v in data:
        byte_value |= (v & mask) << shift
        shift += num_bits
        if shift >= 8:
            byte_values.append(byte_value)
            byte_value = 0
            shift = 0
        count += 1
        if count >= num_nbits:
            break

    # now convert the list of byte values to a "unicode" string
    return bytes(byte_values).decode(encoding='utf_8')

# Code to test the encode/decode functions.
if __name__ == '__main__':
    import sys

    # get test text/filename
    if len(sys.argv) != 2:
        print('Usage: xyzzy.py <text message>')
        sys.exit(1)
    data = sys.argv[1]

    # get file contents if "data" is a filename
    try:
        data = open(data). read()
    except FileNotFoundError:
        pass

    print(f"data=\n'{data}'")

    error = False
    for num_bits in (1, 2, 4, 8):
        encoded_data = encode(data, num_bits)
        result = decode(encoded_data)

        if result != data:
            error = True
            print('Error!  num_bits={num_bits}, result=\n{result}')
            print()

    if not error:
        print('All OK!')
