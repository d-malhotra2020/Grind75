from collections import deque
class HitCounter:

    def __init__(self):
        self.hitCounterVariable = deque()

    def hit(self, timestamp: int) -> None:
        self.hitCounterVariable.append(timestamp)

    def getHits(self, timestamp: int) -> int:
      while self.hitCounterVariable and self.hitCounterVariable[0] <= timestamp - 300:
        self.hitCounterVariable.popleft()
      return len(self.hitCounterVariable)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)