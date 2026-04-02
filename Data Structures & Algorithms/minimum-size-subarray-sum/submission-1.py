class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        windowSum = 0 
        min_length = 1000000

        for right in range(len(nums)):
            windowSum += nums[right]

            while windowSum >= target:
                subarray_length = right - left + 1
                min_length = min(min_length, subarray_length)
                windowSum -= nums[left]
                left += 1
        return min_length if min_length != 1000000 else 0
