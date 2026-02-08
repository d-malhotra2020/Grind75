from collections import deque
class HitCounter:

    def __init__(self):
      self.hitCounter = deque()
        

    def hit(self, timestamp: int) -> None:
      self.hitCounter.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
      while self.hitCounter and self.hitCounter[0] <= timestamp - 300:
        self.hitCounter.popleft()
      return len(self.hitCounter)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)