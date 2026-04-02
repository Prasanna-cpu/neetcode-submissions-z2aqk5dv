class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        n = len(nums)
        result = []

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        for val, f in frequency.items():
            if f > n // 3:
                result.append(val)
        return result