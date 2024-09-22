class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1
        result = 1
        prev = ""
        
        while right < len(arr):
            if arr[right] > arr[right-1] and prev != ">":
                result = max(result, right - left + 1)
                right +=1
                prev = ">"
                
            elif arr[right] < arr[right-1] and prev != "<":
                result = max(result, right- left + 1)
                right +=1
                prev = "<"
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                prev = ""
        return result
                