class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = sorted(list(ransomNote))
        mag = sorted(list(magazine))
        
        for char in mag:
            if ransom and char in ransom[0]: 
                ransom.pop(0)
        if ransom:
            return False
        else:
            return True
                