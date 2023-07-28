class Solution:
    def reverseWords(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        left = 0
        right = 0
        index = 0
        while right < len(s):
            if s[right] != ' ':
                right+=1
            else:
                index = right
                right-=1
                while left <= right:
                    s[left], s[right] = s[right], s[left]
                    left+=1
                    right-=1
                right = index+1
                left = right
        right -=1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1