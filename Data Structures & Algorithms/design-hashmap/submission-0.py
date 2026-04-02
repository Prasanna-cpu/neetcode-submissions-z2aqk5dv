class MyHashMap:

    def __init__(self):
        self.BASE = 1000
        self.data = [[] for _ in range(self.BASE)]

    def _hash(self, key):
        return key % self.BASE

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        for i, (k, v) in enumerate(self.data[h]):
            if k == key:
                self.data[h][i] = (key, value)
                return
        self.data[h].append((key, value))

    def get(self, key: int) -> int:
        h = self._hash(key)
        for (k, v) in self.data[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        self.data[h] = [(k, v) for (k, v) in self.data[h] if k != key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)