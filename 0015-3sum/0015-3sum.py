class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = a + nums[left] + nums[right]
                if total > 0:
                    right -=1
                elif total < 0:
                    left+=1
                else:
                    result.append([a, nums[left], nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return result
            
        