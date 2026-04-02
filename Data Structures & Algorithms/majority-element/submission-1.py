class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        canditate = None
        count = 0 

        for num in nums:
            if count == 0:
                canditate = num
            count += (1 if num == canditate else -1)
        return canditate
        