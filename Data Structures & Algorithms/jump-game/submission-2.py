class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_to_reach = 0

        n = len(nums)

        for i in range(n):
            if i > farthest_to_reach:
                return False
            farthest_to_reach = max(farthest_to_reach, i + nums[i])
        return True