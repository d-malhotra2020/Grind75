class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        dividor = 1
        while x >= dividor*10:
            dividor*=10
        while x:
            right = x%10
            left = x // dividor
            
            if left != right:
                return False
        
            x = (x % dividor) // 10
            dividor = dividor // 100
        return True
        