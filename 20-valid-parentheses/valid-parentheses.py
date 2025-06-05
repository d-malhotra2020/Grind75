class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      hashmap = {")":"(", "]":"[", "}": "{"}
      for character in s:
        if character in hashmap:
          if stack and stack[-1] == hashmap[character]:
            stack.pop()
          else:
            return False
        else:
          stack.append(character)
      return True if not stack else False