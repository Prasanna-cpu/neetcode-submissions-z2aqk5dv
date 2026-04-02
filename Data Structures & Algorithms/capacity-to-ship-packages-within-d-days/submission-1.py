class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isFeasible(capacity):
            days_taken = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    days_taken += 1
                    current_load = 0
                current_load += w

            return days_taken <= days

        left = max(weights)
        right = sum(weights)
        answer = right

        while left <= right:
            mid = left + (right-left)//2
            if isFeasible(mid):
                answer = mid
                right = mid -1
            else:
                left = mid + 1
        return answer
        