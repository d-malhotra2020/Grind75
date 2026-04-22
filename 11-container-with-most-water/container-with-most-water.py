class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        currentMax = 0
        while left < right:
          width = right - left
          min_length = min(height[left], height[right])
          currentArea = width * min_length
          currentMax = max(currentMax, currentArea)
          if height[left] < height[right]:
            left += 1
          else:
            right -= 1
        return currentMax