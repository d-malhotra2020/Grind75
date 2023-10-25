class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub_Array = nums[0]
        currentSum = 0
        
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSub_Array = max(maxSub_Array, currentSum)
        return maxSub_Array