class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
            return False

        result = [0] * 26

        for c1,c2 in zip(s, t):
            result[ord(c1) - ord('a')] += 1
            result[ord(c2) - ord('a')] -= 1

        return all(x == 0 for x in result) 