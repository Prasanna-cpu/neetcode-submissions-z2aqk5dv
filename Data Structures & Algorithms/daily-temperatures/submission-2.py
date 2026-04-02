class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        index_stack = []

        for i,temp in enumerate(temperatures):
            while index_stack and temperatures[i] > temperatures[index_stack[-1]]:
                prev_index = index_stack.pop()
                result[prev_index] = i-prev_index
            index_stack.append(i)

        return result