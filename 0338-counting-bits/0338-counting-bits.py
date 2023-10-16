class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        for i in range(1, n+1):
            halfposition = math.floor(i//2)
            if (i%2 == 1):
                result[i] = result[halfposition]+1
            else:
                result[i] = result[halfposition]
        return result
            