class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)
            if secondStone > firstStone:
                heapq.heappush(stones, (firstStone - secondStone))
        
        stones.append(0)
        return abs(stones[0])