from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        result = []

        count = Counter(s)

        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]

        for ch,freq in count.items():
            result.append(ch * freq)

            
        return "".join(result)
        