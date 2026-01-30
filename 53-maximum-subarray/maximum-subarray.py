class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      currentSum = 0
      maxSum = nums[0]

      for n in nums:
        if currentSum < 0:
          currentSum = 0
        currentSum += n
        maxSum = max(maxSum, currentSum)
      return maxSum