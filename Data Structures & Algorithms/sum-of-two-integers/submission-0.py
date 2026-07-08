class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # 32-bit mask
        MAX_INT = 0x7FFFFFFF   # Maximum positive 32-bit integer

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX_INT else ~(a ^ MASK)