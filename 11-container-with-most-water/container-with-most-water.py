class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        current_max = 0

        while left < right:
          width = right - left
          limiting_height = min(height[left], height[right])
          current_area = width * limiting_height

          current_max = max(current_max, current_area)

          if height[left] < height[right]:
            left += 1
          else:
            right -= 1
        return current_max