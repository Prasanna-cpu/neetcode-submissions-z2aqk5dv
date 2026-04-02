class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        n = len(nums)

        for i , a in enumerate(nums):

            if i > 0 and nums[i - 1] == a:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                three_sum = nums[left] + nums[right] + a

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[right], a])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                       left += 1

                

        return result