class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current = {}
        max_string = 0

        for right in range(len(s)):
          current[s[right]] = current.get(s[right], 0) + 1
          while current[s[right]] > 1:
            current[s[left]] -= 1
            if current[s[left]] == 0:
              del current[s[left]]
            left += 1
          max_string = max(max_string, right - left + 1)
        return max_string
