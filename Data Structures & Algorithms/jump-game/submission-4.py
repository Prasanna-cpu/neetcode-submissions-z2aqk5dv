class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = False
        n = len(nums)

        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach , i + nums[i])
        return True