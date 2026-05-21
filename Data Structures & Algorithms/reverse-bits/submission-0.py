class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Shift result left to make room, then add last bit of n
            result = (result << 1) | (n & 1)
            # Move to next bit of n
            n >>= 1
        return result