class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        distance = float('inf')
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            newTarget = target - nums[i]
            while left < right:
                goal = nums[left] + nums[right]
                if abs(distance) > abs(newTarget - goal):
                    distance = newTarget - goal
                if goal == newTarget:
                    return target
                elif goal < newTarget:
                    left+=1
                elif goal > newTarget:
                    right -=1
        return target - distance
                