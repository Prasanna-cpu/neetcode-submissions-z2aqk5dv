class Solution:
    def maxDifference(self, s: str) -> int:
        
        frequency = {}

        for ch in s:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        
        odd = [num for num in frequency.values() if num % 2 != 0]
        even = [num for num in frequency.values() if num % 2 == 0]

        return max(odd) - min(even)