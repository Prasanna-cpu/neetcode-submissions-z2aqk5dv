class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in nums:
            #If the predecessor number is not in set , start the seq. with current_number
            if num-1 not in num_set:
                length = 1
                current = num+1

                # If its successor is in set , increment teh number and length
                while current in num_set:
                    length += 1
                    current += 1
                # Take the max
                max_length = max(length,max_length)
        return max_length