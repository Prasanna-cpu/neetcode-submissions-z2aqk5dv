class Solution:
    def trap(self, height: List[int]) -> int:
        
            left, right = 0, len(height) - 1
            left_max, right_max = 0, 0
            total_water = 0
            
            while left < right:
                if height[left] < height[right]:
                    # Process left side
                    if height[left] >= left_max:
                        left_max = height[left]  # Update left_max
                    else:
                        total_water += left_max - height[left]  # Add trapped water
                    left += 1
                else:
                    # Process right side
                    if height[right] >= right_max:
                        right_max = height[right]  # Update right_max
                    else:
                        total_water += right_max - height[right]  # Add trapped water
                    right -= 1
            
            return total_water