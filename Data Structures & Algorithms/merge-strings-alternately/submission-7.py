class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        m = len(word1)
        n = len(word2)

        merged_array = []

        while i < m or i < n:

            if i < m:
                merged_array.append(word1[i])
            
            if i < n:
                merged_array.append(word2[i])

            i += 1

        return ''.join(merged_array)

            