class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window_sum = sum(arr[:k])
        count = 0
        target = k * threshold

        if window_sum >= target:
            count += 1

        n = len(arr)

        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target:
                count += 1
        
        return count