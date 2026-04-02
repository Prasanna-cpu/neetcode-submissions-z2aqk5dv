class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        merged = [intervals[0]]

        for current_interval in intervals[1:]:
            previous_interval = merged[-1]

            if current_interval[0] <= previous_interval[1]:
                previous_interval[1] = max(previous_interval[1], current_interval[1])
            else:
                merged.append(current_interval)
        
        return merged