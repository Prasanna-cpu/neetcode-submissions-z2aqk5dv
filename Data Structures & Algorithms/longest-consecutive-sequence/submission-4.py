class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        max_length = 0
        current_length = 0

        for num in nums:
            if num - 1 not in seen:
                current_length = 1
                current_num = num

                while current_num + 1 in seen:
                    current_length += 1
                    current_num += 1
                
                max_length = max(max_length, current_length)
        
        return max_length