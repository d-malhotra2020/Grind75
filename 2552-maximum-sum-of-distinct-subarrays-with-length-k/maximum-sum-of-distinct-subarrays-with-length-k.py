class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        current = 0
        max_score = float('-inf')
        left = 0
        freq = {}

        for right in range(len(nums)):
          current += nums[right]
          freq[nums[right]] = freq.get(nums[right], 0) + 1
          if right - left + 1 == k:
            if len(freq) == k:
              max_score = max(max_score, current)
            current -= nums[left]
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
              del freq[nums[left]]
            left += 1
        return 0 if max_score == float('-inf') else max_score

