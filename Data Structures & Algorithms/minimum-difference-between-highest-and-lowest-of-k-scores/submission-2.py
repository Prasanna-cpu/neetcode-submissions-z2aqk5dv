class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if k == 1:
            return 0
        min_diff = float("inf")
        n = len(nums)

        for i in range(n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)
        return min_diff