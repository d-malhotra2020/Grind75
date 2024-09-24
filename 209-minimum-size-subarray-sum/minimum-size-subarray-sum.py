class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        length = float("inf")
        
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                length = min(right - left + 1, length)
                total -= nums[left]
                left += 1
        return 0 if length == float("inf") else length