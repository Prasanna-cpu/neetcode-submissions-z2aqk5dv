class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(nums):
            prev = 0
            curr = 0

            for num in nums:
                prev, curr = curr , max(curr, prev + num)

            return curr

        exclude_first_house = rob_linear(nums[1:])
        exclude_last_house = rob_linear(nums[:-1])

        return max(exclude_first_house, exclude_last_house)