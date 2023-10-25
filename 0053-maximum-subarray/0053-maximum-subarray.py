class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumSubArray = nums[0]
        currentSum = 0
        
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maximumSubArray = max(maximumSubArray, currentSum)
        return maximumSubArray