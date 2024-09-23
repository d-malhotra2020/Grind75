class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currentSum = sum(arr[:k])
        result = 0
        
        for i in range(len(arr) - k + 1):
            if (currentSum / k) >= threshold:
                result += 1
            if i + k < len(arr):
                currentSum += arr[i+k] - arr[i]
        return result