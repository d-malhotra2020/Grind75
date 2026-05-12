class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxSum):
            subArray = 1
            currentSum = 0
            for n in nums:
                if currentSum + n > maxSum:
                    subArray += 1
                    currentSum = n
                else:
                    currentSum += n
            return subArray <= k

        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) //2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left
