class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        for i in range(len(nums)):
          if currentSum < 0:
            currentSum = 0
          currentSum+=nums[i]
          maxSum = max(maxSum, currentSum)
        return maxSum
