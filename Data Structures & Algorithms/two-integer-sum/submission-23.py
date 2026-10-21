class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for i , num in enumerate(nums):
            delta = target - num
            if delta in mapper:
                return [mapper[delta], i]
            mapper[num] = i