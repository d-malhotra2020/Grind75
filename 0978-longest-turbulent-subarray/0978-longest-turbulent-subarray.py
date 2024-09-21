class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1
        result = 1
        prev = ""
        
        while right < len(arr):
            if arr[right-1] > arr[right] and prev != ">":
                result = max(result, right - left + 1)
                prev = ">"
                right +=1
            elif arr[right-1] < arr[right] and prev != "<":
                result = max(result, right - left + 1)
                prev = "<"
                right += 1
            else:
                right = right + 1 if arr[right] == arr[right-1] else right
                left = right - 1
                prev = ""
        return result
                