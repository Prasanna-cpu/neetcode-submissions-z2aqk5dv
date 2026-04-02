class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity):
            days_used = 1
            current_load = 0

            for w in weights:
                if current_load + w > capacity:
                    days_used += 1
                    current_load = 0
                current_load += w
            
            return days_used <= days

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if canShip(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans