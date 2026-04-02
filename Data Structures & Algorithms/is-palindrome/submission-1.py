class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = ''.join(char.lower() for char in s if char.isalnum())
        return refined == refined[::-1]
        