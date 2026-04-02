class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        def findFirst(nums, target):
            left = 0
            right = n - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2
                middle_element = nums[mid]

                if middle_element == target:
                    first = mid
                    right = mid - 1
                elif middle_element < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return first
        
        def findLast(nums, target):
            left = 0
            right = n - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2
                middle_element = nums[mid]

                if middle_element == target:
                    last = mid
                    left = mid + 1

                elif middle_element < target:
                    left = mid + 1
                
                else:
                    right = mid - 1

            return last
        

        return [findFirst(nums, target), findLast(nums, target)]




