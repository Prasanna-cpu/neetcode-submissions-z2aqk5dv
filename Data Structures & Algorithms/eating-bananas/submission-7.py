class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            if canEat(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low