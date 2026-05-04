class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      nonZero = 0
      for i in range(len(nums)):
        if nums[i] != 0:
          nums[i], nums[nonZero] = nums[nonZero], nums[i]
          nonZero += 1
      