class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        majority = len(nums) // 2

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num , f in freq.items():
            if freq[num] > majority:
                return num
        
