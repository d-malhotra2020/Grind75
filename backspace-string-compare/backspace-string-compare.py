class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_out = []
        t_out = []

        for char in s:
            if char == "#":
                if s_out:
                    s_out.pop()
            else:
                s_out.append(char)
        for char in t:
            if char == "#":
                if t_out:
                    t_out.pop()
            else:
                t_out.append(char)
        if s_out == t_out:
            return True
        else:
            return False