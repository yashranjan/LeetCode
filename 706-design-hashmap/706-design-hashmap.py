class Bucket:
    def __init__(self):
        self.bucket = []
        
    def put(self, key, val):
        found = 0
        for item in self.bucket:
            if item[0] == key:
                item[1] = val
                found = 1
        if not found:
            self.bucket.append([key, val])
    
    def get(self, key):
        ans = -1
        for k, v in self.bucket:
            if k == key:
                ans = v
                break
        return ans
    
    def remove(self, key):
        for item in self.bucket:
            if item[0] == key:
                item[1] = -1

    
class MyHashMap:

    def __init__(self):
        self.hashKey = 2069
        self.hashMap = [Bucket() for i in range(self.hashKey)]

    def put(self, key: int, value: int) -> None:
        self.hashMap[key%self.hashKey].put(key, value)

    def get(self, key: int) -> int:
        return self.hashMap[key%self.hashKey].get(key)

    def remove(self, key: int) -> None:
        self.hashMap[key%self.hashKey].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)