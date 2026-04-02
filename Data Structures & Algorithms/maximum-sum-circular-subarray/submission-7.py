class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0

        curr_max = 0
        curr_min = 0

        max_sum = nums[0]
        min_sum = nums[0]

        for n in nums:
            curr_max = max(curr_max + n , n)
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min + n, n)
            min_sum = min(min_sum, curr_min)

            total_sum += n

        if max_sum < 0:
            return max_sum
        else:
            return max(max_sum, total_sum - min_sum)