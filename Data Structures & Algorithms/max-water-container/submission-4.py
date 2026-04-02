class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        max_area = 0

        while left < right:

            area = min(heights[right], heights[left]) * (right - left)

            max_area = max(area, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area