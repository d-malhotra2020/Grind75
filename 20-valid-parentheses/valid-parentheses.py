class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"]":"[", "}":"{", ")":"("}
        for characters in s:
            if characters in hashmap:
                if stack and stack[-1] in hashmap[characters]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(characters)
        return True if not stack else False