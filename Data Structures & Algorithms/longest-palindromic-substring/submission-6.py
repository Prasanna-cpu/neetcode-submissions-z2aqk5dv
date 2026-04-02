class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(string, i, j):
            while i >= 0 and j < len(string) and string[i] == string[j]:
                i -= 1
                j += 1
            return string[i + 1 : j]

        max_length = ""

        for i in range(len(s)):
            max_length = max(
                max_length,
                is_palindrome(s, i, i),
                is_palindrome(s, i, i + 1),
                key = len
            )

        return max_length
