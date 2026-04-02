class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        n = len(senate)

        rqueue = deque()
        dqueue = deque()

        for i , s in enumerate(senate):
            if s == 'R':
                rqueue.append(i)
            else:
                dqueue.append(i)

        while rqueue and dqueue:

            r_idx = rqueue.popleft()
            d_idx = dqueue.popleft()

            if r_idx < d_idx:
                rqueue.append(r_idx + n)
            else:
                dqueue.append(d_idx + n)
        return "Radiant" if rqueue else "Dire"