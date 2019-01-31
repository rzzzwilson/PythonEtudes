"""
A class to accumulate an N bit stream into a string.
"""

class DecodeBits:
    """A class that accumulates a stream of N bit values into a string."""

    def __init__(self, num_bits):
        """Initialize the accumulator class.

        num_bits  the number of bits in the stream values.
                  (must be one of 1, 2, 4 or 8)
        """

        if num_bits not in [1, 2, 4, 8]:
            raise ValueError(f"Bad value for 'num_bits', got {num_bits}, "
                              "expected one of 1, 2, 4 or 8.")

        self.numn_bits = num_bits
        self._clear()

    def put(self, bits):
        """Put an N bit value into the accumulator.

        bits  the N bit value to accumulate
        """

        self.accum += (bits << self.shift)
        self.shift += self.numn_bits
        if self.shift >= 8:
            self.result += chr(self.accum)
            self.accum = 0
            self.shift = 0

    def get(self):
        """Returns the accumulated string and resets the accumuator."""

        result = bytes(self.result).decode(encoding='utf_8')
        self._clear()
        return result

    def _clear(self):
        """Internal method to clear the accumulator state."""

        self.accum = 0
        self.shift = 0
        self.result = ''

if __name__ == '__main__':
    data = [1, 2, 0, 1, 0, 1, 3, 1,    # the 2bit-encoded message
            0, 0, 2, 0, 3, 1, 3, 1,
            3, 3, 2, 1, 2, 0, 3, 1,
            3, 2, 2, 1, 3, 0, 3, 1,
            1, 0, 2, 0]
    
    decoder = DecodeBits(2)
    for val in data:
        decoder.put(val)
    print(decoder.get())

    # test that .get() resets the decoder properly
    for val in data:
        decoder.put(val)
    print(decoder.get())
    
