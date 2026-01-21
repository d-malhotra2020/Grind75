from collections import deque
class HitCounter:

    def __init__(self):
      self.hitCounterVar = deque()
        

    def hit(self, timestamp: int) -> None:
      self.hitCounterVar.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hitCounterVar and self.hitCounterVar[0] <= timestamp - 300:
          self.hitCounterVar.popleft()
        return len(self.hitCounterVar)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)