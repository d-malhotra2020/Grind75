class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        current = {}
        max_freq = 0
        max_string = 0

        for right in range(len(s)):
          current[s[right]] = current.get(s[right], 0) + 1
          max_freq = max(max_freq, current[s[right]])
          if k + max_freq < right - left + 1:
            current[s[left]] -= 1
            left += 1
          max_string = max(max_string, right - left + 1)
        return max_string
        