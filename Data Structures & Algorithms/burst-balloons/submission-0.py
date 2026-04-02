class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create DP table
        dp = [[0] * n for _ in range(n)]
        
        # Length of subarray to consider
        for length in range(2, n):  # length of window
            for left in range(n - length):
                right = left + length
                # Try bursting each balloon in (left, right) last
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + nums[left] * nums[k] * nums[right] + dp[k][right]
                    )
        
        # Final result is bursting all between (0, n-1)
        return dp[0][n - 1]
        