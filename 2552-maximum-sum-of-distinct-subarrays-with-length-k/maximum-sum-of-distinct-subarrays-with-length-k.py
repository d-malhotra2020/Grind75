class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float('-inf')
        left = 0
        currentSum = 0
        freq = {}

        for right in range(len(nums)):
          currentSum += nums[right]
          freq[nums[right]] = freq.get(nums[right], 0) + 1
          if right - left + 1 == k:
            if k == len(freq):
              max_sum = max(max_sum, currentSum)
            currentSum -= nums[left]
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
              del freq[nums[left]]
            left += 1
        return 0 if max_sum == float('-inf') else max_sum
          