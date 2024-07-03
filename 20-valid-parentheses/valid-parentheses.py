class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "]":"[", "}":"{"}
        for close in s:
            if close in hashmap:
                if stack and stack[-1] == hashmap[close]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(close)
        return True if not stack else False