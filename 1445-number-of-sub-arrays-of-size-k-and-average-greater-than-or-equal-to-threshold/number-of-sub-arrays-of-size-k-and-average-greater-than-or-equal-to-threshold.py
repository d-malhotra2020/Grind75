class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        result = 0
        currentSum = sum(arr[:k-1])
        
        for left in range(len(arr) - k + 1):
            currentSum += arr[left + k - 1]
            if (currentSum/k) >= threshold:
                result += 1
            currentSum -= arr[left]
        return result
            
            
            