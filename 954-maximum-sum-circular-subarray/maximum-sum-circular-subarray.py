class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        currentMax = 0
        currentMin = 0
        total = 0
        
        for n in nums:
            currentMax = max(currentMax + n, n)
            currentMin = min(currentMin + n, n)
            globalMax = max(globalMax, currentMax)
            globalMin = min(globalMin, currentMin)
            total += n
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax