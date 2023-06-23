class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        i = 0
        sign = 1
        if s[i] == '+':
            i+=1
        elif s[i] == '-':
            i+=1
            sign = -1
        parsing = 0
        while i < len(s):
            current = s[i]
            if not current.isdigit():
                break
            else:
                parsing = parsing * 10 + int(current)
            i+=1
        parsing = parsing * sign
        if parsing > 2**31 - 1:
            return 2**31 - 1
        elif parsing <= -2**31:
            return -2**31
        else:
            return parsing


