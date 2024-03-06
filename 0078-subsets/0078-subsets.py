class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def dfs(index):
            if index >= len(nums):
                result.append(current.copy())
                return
            
            #decision to include nums[index]
            current.append(nums[index])
            dfs(index+1)
            current.pop()
            dfs(index+1)
            
        dfs(0)
        return result
            