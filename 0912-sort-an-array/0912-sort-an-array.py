class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums
    def mergeSort(self, nums: List[int]):
        if len(nums) > 1:
            
            mid = (len(nums)//2)
            left = nums[:mid]
            right = nums[mid:]
        
            self.mergeSort(left)
            self.mergeSort(right)
        
            i = 0 
            j = 0
            k = 0
        
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i+=1    
                else:
                    nums[k] = right[j]
                    j+=1
                k+=1
            while i < len(left):
                    nums[k] = left[i]
                    i+=1
                    k+=1
            while j < len(right):
                    nums[k] = right[j]
                    j+=1
                    k+=1    
        