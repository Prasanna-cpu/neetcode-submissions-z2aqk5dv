class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        majority_nums = len(nums) // 3
        result = []

        for num , times in freq.items():
            if times > majority_nums:
                result.append(num)
        return result