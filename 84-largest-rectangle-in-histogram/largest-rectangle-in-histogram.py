class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)

        max_area = 0
        for i, height in enumerate(heights):
          start = i
          while stack and height < stack[-1][0]:
            h, j = stack.pop()
            w = i - j
            area = h * w
            max_area = max(max_area, area)
            start = j
          stack.append((height, start))

        while stack: 
          h, j = stack.pop()
          w = n - j
          max_area = max(max_area, h * w)
        return max_area