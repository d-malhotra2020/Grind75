class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        characterSet = set()
        
        for right in range(len(s)):
            while s[right] in characterSet:
                characterSet.remove(s[left])
                left+=1
            characterSet.add(s[right])
            result = max(result, right - left + 1)
        return result
                