class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        refined_string = ''.join(char.lower() for char in s if char.isalnum())
        return refined_string == refined_string[::-1]