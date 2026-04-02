class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        answer = right

        def can_ship(capacity):
            total = 0
            day_count = 1
            for w in weights:
                total += w
                if total > capacity:
                    day_count += 1
                    total = w
            return day_count <= days

        while left <= right:
            mid = (left + right)//2
            if can_ship(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
        