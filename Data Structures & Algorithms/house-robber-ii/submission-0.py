class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            prev = 0
            curr = 0
            for money in houses:
                prev,curr = curr,max(curr,prev+money)
            return curr
        
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)

        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])
        return max(case1,case2)