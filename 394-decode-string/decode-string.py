class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_number = 0
        current_string = ""

        for char in s:
          if char == "[":
            stack.append(current_number)
            stack.append(current_string)
            current_number = 0
            current_string = ""
          elif char == "]":
            prev_string = stack.pop()
            number = stack.pop()
            current_string = prev_string + number * current_string
          elif char.isdigit():
            current_number = current_number * 10 + int(char)
          else:
            current_string += char
        return current_string
