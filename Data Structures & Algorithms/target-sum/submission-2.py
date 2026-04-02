class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            if (index,current_sum) in memo:
                return memo[(index,current_sum)]
            
            positive = backtrack(index+1,current_sum+nums[index])
            negative = backtrack(index+1,current_sum-nums[index])

            memo[(index,current_sum)] = positive+negative
            return memo[(index,current_sum)]
        return backtrack(0,0)
        