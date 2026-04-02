class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0
        heights.append(0)

        for i , h in enumerate(heights):

            while stack and heights[stack[-1]] > h:

                top_index = stack.pop()
                height = heights[top_index]

                if not stack:
                    width = i
                else:
                    width = i - 1 - stack[-1]

                area = height * width
                max_area = max(area , max_area)

            
            stack.append(i)
        return max_area