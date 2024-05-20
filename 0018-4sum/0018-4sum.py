class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        quad = []
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums)- k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            left = start
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] < target:
                    left+=1
                elif nums[left] + nums[right] > target:
                    right -=1
                else:
                    output.append(quad + [nums[left], nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        kSum(4, 0, target)
        return output