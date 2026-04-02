class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {ch: i for i, ch in enumerate(s)}
        result = []

        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
        