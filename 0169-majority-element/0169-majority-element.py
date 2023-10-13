class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for n in nums:
            if count == 0:
                result = n
            count+=(1 if n == result else -1)
        return result