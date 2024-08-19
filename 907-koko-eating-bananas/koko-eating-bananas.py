class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        
        while (left <= right):
            k = (left + right)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                right = k - 1
                result = min(result, k)
            else:
                left = k + 1
        return result