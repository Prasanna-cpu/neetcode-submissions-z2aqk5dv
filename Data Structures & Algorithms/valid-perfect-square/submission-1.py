class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            answer = mid * mid

            if answer == num:
                return True
            
            elif answer < num:
                left = mid + 1

            else:
                right = mid - 1

        return False
