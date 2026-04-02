class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        n = len(s)

        def expand(left, right):
            palindrome_count = 0

            while left >= 0 and right < n and s[left] == s[right]:
                palindrome_count += 1
                left -= 1
                right += 1
            return palindrome_count
        
        for i in range(n):
            count += expand(i, i)
            count += expand(i, i + 1)
             
        return count