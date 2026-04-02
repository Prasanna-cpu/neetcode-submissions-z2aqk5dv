class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        refined_string = ''.join(ch.lower() for ch in s if ch.isalnum())
        return refined_string == refined_string[::-1]