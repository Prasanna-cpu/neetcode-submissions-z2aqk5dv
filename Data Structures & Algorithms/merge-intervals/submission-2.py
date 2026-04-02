class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            previous = merged[-1]
            if interval[0] <= previous[1]:
                previous[1] = max(interval[1],previous[1])
            else:
                merged.append(interval)
        return merged

        