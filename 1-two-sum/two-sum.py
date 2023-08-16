class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in hashmap:
                return [hashmap[goal], i]
            hashmap[nums[i]] = i