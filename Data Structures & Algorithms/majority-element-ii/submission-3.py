class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        frequency = {}
        n = len(nums)
        majority = n // 3
        result = []

        for num in nums:
            frequency[num] = frequency.get(num,0) + 1
        
        for k,v in frequency.items():
            if v > majority:
                result.append(k)
        return result

        