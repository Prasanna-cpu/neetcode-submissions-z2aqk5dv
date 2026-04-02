class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapper:
                return [mapper[complement], i]
            mapper[nums[i]] = i
    