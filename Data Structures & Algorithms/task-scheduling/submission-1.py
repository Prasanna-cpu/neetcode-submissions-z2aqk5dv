class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_count = sum(1 for freq in task_counts.values() if freq == max_freq)

        part_count = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), part_count)