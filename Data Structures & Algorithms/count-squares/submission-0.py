from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)

    def add(self, point):
        x, y = point
        self.pointCount[(x, y)] += 1

    def count(self, point):
        x, y = point
        total = 0

        for (x1, y1), freq in self.pointCount.items():
            if x1 == x and y1 == y:
                continue

            # Check if they are on the same column
            if abs(x1 - x) == abs(y1 - y) and x != x1 and y != y1:
                # Two other corners of the square
                p2 = (x1, y)
                p3 = (x, y1)

                total += (
                    self.pointCount.get(p2, 0)
                    * self.pointCount.get(p3, 0)
                    * freq
                )
        return total
