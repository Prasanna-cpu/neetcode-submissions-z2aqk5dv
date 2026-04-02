class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque([0])

        while queue:
            current_node = queue.popleft()
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return len(visited) == n