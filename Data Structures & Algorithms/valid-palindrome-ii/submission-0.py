class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = lambda sub: sub == sub[::-1]

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])
            left += 1
            right -= 1

        return True
        