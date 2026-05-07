class Solution:
    def decodeString(self, s: str) -> str:
        current_string = ""
        stack = []
        current_num = 0

        for char in s:
          if char == "[":
            current_num = stack.append(current_num)
            current_string = stack.append(current_string)
            current_num = 0
            current_string = ""
          elif char == "]":
            prev_string = stack.pop()
            num = stack.pop()
            current_string = prev_string + num * current_string
          elif char.isdigit():
            current_num = current_num * 10 + int(char)
          else:
            current_string += char
        return current_string