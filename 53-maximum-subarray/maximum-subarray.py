class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumArray = nums[0]
        currentMax = 0
        
        for n in nums:
            if currentMax < 0:
                currentMax = 0
            currentMax += n
            maximumArray = max(maximumArray, currentMax)
        return maximumArray
            