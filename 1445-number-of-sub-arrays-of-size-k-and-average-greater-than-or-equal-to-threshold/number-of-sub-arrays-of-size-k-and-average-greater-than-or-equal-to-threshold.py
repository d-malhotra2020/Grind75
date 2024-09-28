class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        currentSum = sum(arr[:k])
        
        for i in range(len(arr) - k + 1):
            if (currentSum / k) >= threshold:
                result += 1
            if (i + k) < len(arr):
                currentSum += arr[i + k] - arr[i]
        return result