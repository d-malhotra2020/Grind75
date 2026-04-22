class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for a in range(len(nums)-1, 1, -1):
          b = 0
          c = a - 1
          while b < c:
            if nums[b] + nums[c] > nums[a]:
              result += c - b
              c -= 1
            else:
              b += 1
        return result