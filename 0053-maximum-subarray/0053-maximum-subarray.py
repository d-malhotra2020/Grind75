class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        current = 0
        
        for n in nums:
            if current < 0:
                current = 0
            current += n
            maximum = max(maximum, current)
        return maximum