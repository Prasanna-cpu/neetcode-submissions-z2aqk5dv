class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1
        current_sum = -1

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum