class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumArray = nums[0]
        current = 0
        
        for n in nums:
            if current < 0:
                current = 0
            current += n
            maximumArray = max(maximumArray, current)
        return maximumArray