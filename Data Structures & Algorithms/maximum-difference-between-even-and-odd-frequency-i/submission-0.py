class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        odd_freq = [num for num in freq.values() if num%2 == 1]
        even_freq = [num for num in freq.values() if num%2 == 0]

        return max(odd_freq) - min(even_freq)