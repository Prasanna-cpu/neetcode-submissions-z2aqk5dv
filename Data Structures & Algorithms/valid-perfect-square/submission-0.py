class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        left = 0
        right = num // 2

        while left <= right:
            mid = (left + right)//2
            target = mid * mid

            if num == target:
                return True
            elif target < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
