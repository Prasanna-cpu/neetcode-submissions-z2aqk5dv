class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sum_of_squares(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squares(n)

        return True