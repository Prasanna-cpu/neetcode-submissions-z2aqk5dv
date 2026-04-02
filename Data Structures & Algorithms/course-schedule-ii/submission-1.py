class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)
            for n in graph[course]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)

        return result if len(result) == numCourses else []