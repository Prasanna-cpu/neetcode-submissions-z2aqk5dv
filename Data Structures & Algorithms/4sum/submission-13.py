class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        seen = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                l = j + 1
                r = n - 1

                while l < r:
                    target_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if target_sum < target:
                        l += 1
                    elif target_sum > target:
                        r -= 1
                    else:
                        seen.add((nums[l], nums[r], nums[i], nums[j]))
                        l += 1
                        r -= 1
        return list(seen)