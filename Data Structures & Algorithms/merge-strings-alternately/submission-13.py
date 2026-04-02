class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        m = len(word1)
        n = len(word2)
        result = []

        while i < m or i < n:
            if i < m:
                result.append(word1[i])
            if i < n:
                result.append(word2[i])
            
            i += 1
        return ''.join(result)