class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palindrome(string, i, j):
            while i >= 0 and j < len(string) and string[i] == string[j]:
                i -= 1
                j += 1
            return string[i + 1 : j]
        
        max_length_str = ""

        for i in range(len(s)):
            max_length_str = max(max_length_str, palindrome(s, i, i), palindrome(s, i, i+ 1), key = len)
        
        return max_length_str