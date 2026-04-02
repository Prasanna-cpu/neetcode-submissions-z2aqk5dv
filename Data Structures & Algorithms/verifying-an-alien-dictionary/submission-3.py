class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char : i for i, char in enumerate(order)}
        
        for i in range(len(words)-1):
            word1 ,  word2 = words[i] , words[i+1]
            min_length = min(len(word1), len(word2))
            found_diff = False

            for j in range(min_length):
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    found_diff = True
                    break

            if not found_diff and len(word1) > len(word2):
                return False
        return True