class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_output = []
        t_output = []
        
        for char in s:
            if char == "#":
                if s_output:
                    s_output.pop()
            else:
                s_output.append(char)
        for char in t:
            if char == "#":
                if t_output:
                    t_output.pop()
            else:
                t_output.append(char)
        if s_output == t_output:
            return True
        else:
            return False