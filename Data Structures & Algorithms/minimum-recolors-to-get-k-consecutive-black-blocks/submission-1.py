class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        current_w = sum(1 for i in range(k) if blocks[i] == 'W')
        min_recolors = current_w

        for i in range(k,n):
            if blocks[i - k] == 'W':
                current_w -= 1
            if blocks[i] == 'W':
                current_w += 1
            min_recolors = min(min_recolors, current_w)
        return min_recolors