class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteSorted = sorted(list(ransomNote))
        magazineSorted = sorted(list(magazine))
        
        for char in magazineSorted:
            if ransomNoteSorted and char in ransomNoteSorted[0]:
                ransomNoteSorted.pop(0)
        if ransomNoteSorted:
                return False
        else:
                return True
            
            