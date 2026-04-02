class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat_all(rate):
            total_hrs = 0
            for pile in piles:
                total_hrs+=math.ceil(pile/rate)
            return total_hrs<=h

        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            mid = (left+right) // 2
            if can_eat_all(mid):
                answer = mid
                right = mid-1
            else:
                left = mid+1
        return answer
        