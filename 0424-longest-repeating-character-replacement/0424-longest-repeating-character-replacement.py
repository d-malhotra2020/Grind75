class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmapCount = {}
        result = 0
        
        left = 0
        
        for right in range(len(s)):
            hashmapCount[s[right]] = 1 + hashmapCount.get(s[right], 0)
            while (right - left + 1) - max(hashmapCount.values()) > k:
                hashmapCount[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result