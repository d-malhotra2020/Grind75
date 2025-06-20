class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      counterT = {}
      counterS = {}
      for i in range(len(s)):
        counterS[s[i]] = 1 + counterS.get(s[i], 0)
        counterT[t[i]] = 1 + counterT.get(t[i], 0)
      
      for j in counterS:
        if counterS[j] != counterT.get(j, 0):
          return False
      return True

        