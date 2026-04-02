class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(maxSum):
            count = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > maxSum:
                    count += 1
                    current_sum = num

                else:
                    current_sum += num

            return count <= k

        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        
        return low