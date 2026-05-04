class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k == len(cardPoints):
          return total

        left = 0
        max_score = float('-inf')
        current = 0

        for right in range(len(cardPoints)):
          current += cardPoints[right]
          if right - left + 1 == len(cardPoints) - k:
            max_score = max(total - current, max_score)
            current -= cardPoints[left]
            left += 1
        return max_score

        