class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxSum):
            subarray = 1
            currentSum = 0
            for n in nums:
                if currentSum + n > maxSum:
                    subarray += 1
                    currentSum = n
                else:
                    currentSum += n
            return subarray <= k
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left
