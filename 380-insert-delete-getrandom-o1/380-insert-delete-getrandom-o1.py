class RandomizedSet:

    def __init__(self):
        self.keys = []
        self.keyToInd = {}

    def insert(self, val: int) -> bool:
        if val not in self.keyToInd:
            self.keys.append(val)
            self.keyToInd[val] = len(self.keys)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.keyToInd:
            idx, lastElement = self.keyToInd[val], self.keys[-1]
            self.keyToInd[lastElement], self.keys[idx] = idx, lastElement
            del self.keyToInd[val]
            self.keys.pop()
            return True
        return False

    def getRandom(self) -> int:
        from random import choice
        return choice(self.keys)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()