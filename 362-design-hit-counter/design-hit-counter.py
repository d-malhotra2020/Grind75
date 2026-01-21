class HitCounter:

    def __init__(self):
      self.hitCounterVariable = []

    def hit(self, timestamp: int) -> None:
      self.hitCounterVariable.append(timestamp)
      
    def getHits(self, timestamp: int) -> int:
      left = 0
      right = len(self.hitCounterVariable) - 1
      target = timestamp - 300
      while left <= right:
        mid = (left + right)//2
        if self.hitCounterVariable[mid] <= target:
          left = mid + 1
        else:
          right = mid - 1
      return len(self.hitCounterVariable) - left
            


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)