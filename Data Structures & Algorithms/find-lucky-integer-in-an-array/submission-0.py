from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        frequency = Counter(arr)
        lucky = -1

        for num , count in frequency.items():
            if count == num:
                lucky = max(num, lucky)
        
        return lucky if lucky != -1 else -1


        