class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for character in s:
          if character.isalnum():
            newString += character.lower()
        return newString == newString[::-1]