class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_str = ''.join(ch.lower() for ch in s if ch.isalnum())
        return refined_str == refined_str[::-1]
        