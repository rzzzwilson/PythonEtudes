"""
A generator function encoding a string into an iterator of N bit values.
"""

def encode_string(data, num_bits):
    """Initialize the bit_stream() generator.

    data      the string to stream as N bits at a time
    num_bits  the number of bits to stream (1, 2, 4 or 8)

    Streams N bit values that include encoding data plus the string.

    The first 8 values are the number of bits in the following encoding.
    The next 2*8/num_bits values are the number of characters in the byte string
    The final values are the original data string, in bytestring format, num_bits
    at a time.
    """

    # we will actually send the bytestring form of the string
    # this makes handling of unicode easier
    byte_data = bytes(data, 'utf-8')

    # we first stream the number of bits the following encoding uses
    # send this as 1 bit values, a 1 byte integer value
    i_data = num_bits
    for _ in range(8):
        yield i_data & 0b1
        i_data >>= 1

    # now stream number of bytes in the 'byte_data' bytestring
    # send this as an integer of 2 bytes, 'num_bits' at a time
    num_bytes = len(byte_data)
    mask = 2**num_bits - 1
    for _ in range(2*8//num_bits):
        yield num_bytes & mask
        num_bytes >>= num_bits

    # now stream the entire bytestring of data
    for ch in byte_data:
        for _ in range(8//num_bits):
            yield ch & mask
            ch >>= num_bits

def decode_data(data):
    """Decode a sequence of values that were encoded by 'bits_tostring'.

    data  the list of values to decode
    """

    # first, accumulate the first 8 values as 1 bits (num_bits)
    num_bits = 0
    shift = 0
    for v in data[:8]:
        num_bits = num_bits | (v << shift)
        shift += 1

    # now we get the byte count from the next 2*8/num_bits values
    num_bytes = 0
    shift = 0
    for v in data[8:8 + 2*8//num_bits]:
        num_bytes |= v << shift
        shift += num_bits

    # now collect the remaining values into a bytestring
    num_values = num_bytes * 8//num_bits
    byte_values = []
    byte_value = 0
    shift = 0
    for v in data[8 + 2*8//num_bits:]:
        byte_value |= v << shift
        shift += num_bits
        if shift >= 8:
            byte_values.append(byte_value)
            byte_value = 0
            shift = 0
            if len(byte_values) >= num_values:
                break

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

    print(f'number_of_bits={number_of_bits}')

    encoded_data = list(encode_string(data, number_of_bits))
    print(f'len(encoded_data)={len(encoded_data)}')
    result = decode_data(encoded_data)
    print(f"result='{result}'")

