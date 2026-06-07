class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        results = []

        while left <= right:
            if nums[left] * nums[left] >= nums[right] * nums[right]:
                results.append(nums[left]*nums[left])
                left += 1
            else:
                results.append(nums[right]*nums[right])
                right -= 1
        return results[::-1]