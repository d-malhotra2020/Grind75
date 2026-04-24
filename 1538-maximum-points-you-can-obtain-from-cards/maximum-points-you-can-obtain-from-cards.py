class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k == len(cardPoints):
          return total


        left = 0
        currentState = 0
        max_points = float('-inf')
        for right in range(len(cardPoints)):
          currentState += cardPoints[right]
          if right - left + 1 == len(cardPoints) - k:
            max_points = max(total - currentState, max_points)
            currentState -= cardPoints[left]
            left += 1

        return max_points

