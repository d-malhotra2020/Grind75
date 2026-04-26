class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
      total = sum(cardPoints)
      if k == len(cardPoints):
        return total
      max_score = float('-inf')
      current = 0
      left = 0
      for right in range(len(cardPoints)):
        current += cardPoints[right]
        if right - left + 1 == len(cardPoints) - k:
          max_score = max(max_score, total - current)
          current -= cardPoints[left]
          left += 1
      return max_score
