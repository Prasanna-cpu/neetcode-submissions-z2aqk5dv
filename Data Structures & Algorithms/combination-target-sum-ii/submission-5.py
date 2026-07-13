class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def backtrack(start, path, target):
            if target == 0:
                result.append(path[:])
                return

            length = len(candidates)

            for i in range(start, length):

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > target:
                    break

                backtrack(i + 1 , path + [candidates[i]], target - candidates[i])

        backtrack(0 , [] , target)
        return result
