class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        def backtrack(start , path):
            result.append(path[:])
            n = len(nums)
            
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i + 1, path + [nums[i]])

        backtrack(0,[])
        return result