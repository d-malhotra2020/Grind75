class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArray = nums[0]
        current = 0
        
        for n in nums:
            if current < 0:
                current = 0
            current += n
            maxArray = max(maxArray, current)
        return maxArray
            