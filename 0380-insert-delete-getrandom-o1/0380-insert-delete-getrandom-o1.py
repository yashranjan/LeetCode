class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.st = set()

    def insert(self, val: int) -> bool:
        if val in self.st:
            return False
        self.st.add(val)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.st:
            return False
        self.st.remove(val)
        return True

    def getRandom(self) -> int:
        val = 2**31
        while val not in self.st:
            val = random.choice(self.lst)
        return val