class TimeMap:

    def __init__(self):
      self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
      if key not in self.store:
        self.store[key] = []
      self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
      result = ""
      value = self.store.get(key, [])
      left = 0
      right = len(value) - 1
      while left <= right:
        mid = (left + right)//2
        if value[mid][0] <= timestamp:
          result = value[mid][1]
          left = mid + 1
        else:
          right = mid - 1
      return result
    
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)