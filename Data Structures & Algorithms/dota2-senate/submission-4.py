class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue = deque()
        dQueue = deque()
        n = len(senate)

        for i , s in enumerate(senate):
            if s == 'R':
                rQueue.append(i)
            else:
                dQueue.append(i)

        while rQueue and dQueue:
            r = rQueue.popleft()
            d = dQueue.popleft()

            if r < d:
                rQueue.append(r + n)
            else:
                dQueue.append(d + n)
        
        return "Radiant" if rQueue else "Dire"