class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        m = len(s)
        n = len(t)

        if m != n:
            return False
        
        alphabets = {}

        for ch in s:
            if ch in alphabets:
                alphabets[ch] += 1
            else:
                alphabets[ch] = 1
        
        for ch in t:
            if ch in alphabets:
                alphabets[ch] -= 1
        
        return all(x == 0 for x in alphabets.values())