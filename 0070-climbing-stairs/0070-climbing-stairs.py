class Solution:
    def climbStairs(self, n: int) -> int:
        
        oneStep = 1
        twoStep = 1
        
        for i in range(n-1):
            temp = oneStep
            oneStep = oneStep + twoStep
            twoStep = temp
        return oneStep