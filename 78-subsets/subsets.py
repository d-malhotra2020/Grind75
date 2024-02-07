class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(index):
            if index >= len(nums):
                result.append(subset.copy())
                return
            #decision to include nums[index]
            subset.append(nums[index])
            dfs(index+1)
            
            #decision NOT to include nums[index]
            subset.pop()
            dfs(index+1)
        dfs(0)
        return result