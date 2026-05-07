class Solution:
    def decodeString(self, s: str) -> str:
      stack = []
      current_str = ""
      current_num = 0

      for char in s:
        if char == "[":
          stack.append(current_num)
          stack.append(current_str)
          current_num = 0
          current_str = ""
        elif char == "]":
          prev_string = stack.pop()
          prev_num = stack.pop()
          current_str = prev_string + prev_num * current_str
        elif char.isdigit():
          current_num = current_num * 10 + int(char)
        else:
          current_str += char
      return current_str