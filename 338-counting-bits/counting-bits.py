class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n+1)
        for i in range(1, n+1):
            halfposition = math.floor(i/2)
            if (i%2==1):
                answer[i] = answer[halfposition]+1
            else:
                answer[i] = answer[halfposition]
        return answer