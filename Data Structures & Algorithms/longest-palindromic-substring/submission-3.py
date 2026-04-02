class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(string,i,j):
            while i>=0 and j<len(string) and string[i] == string[j]:
                i -= 1
                j += 1
            return string[i+1:j]

        solution = ""
        for i in range(len(s)):
            solution = max(solution,isPali(s,i,i),isPali(s,i,i+1),key=len)
        return solution