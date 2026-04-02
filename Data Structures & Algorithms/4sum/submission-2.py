class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s = set()
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                l = j + 1
                r = n - 1

                while l < r:

                    sum_total = nums[i] + nums[j] + nums[l] + nums[r]

                    if sum_total < target:
                        l += 1

                    elif sum_total > target:
                        r -= 1

                    elif sum_total == target:
                        s.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return list(s)
        

