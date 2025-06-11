class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
          while left < right and not self.isAlphanumeric(s[left]):
            left += 1
          while right > left and not self.isAlphanumeric(s[right]):
            right -= 1
          if s[left].lower() != s[right].lower():
            return False
          left += 1
          right -= 1
        return True
    
    def isAlphanumeric(self, c):
      return (ord('A') <= ord(c) <= ord('Z') or 
              (ord('a') <= ord(c) <= ord('z') or 
              (ord('0') <= ord(c) <= ord('9'))))

    