# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        end = n
        
        while (first<end):
            mid = (first+end)//2
            if isBadVersion(mid):
                end = mid
            else:
                first = mid + 1
        return first
                