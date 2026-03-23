class Solution:
    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      maxArea = 0

      while left < right:
        width = right - left
        h = min(height[left], height[right])
        currentArea = width * h
        maxArea = max(maxArea, currentArea)

        if height[left] < height[right]:
          left += 1
        else:
          right -= 1
      return maxArea


