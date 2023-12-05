class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        while right < len(nums):
            while right+1 < len(nums) and nums[right+1] == nums[right]:
                right+=1
            nums[left] = nums[right]
            left+=1
            right+=1
        return left
                
        
        