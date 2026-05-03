class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []

        for num , count in freq.items():
            bucket[count].append(num)

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result