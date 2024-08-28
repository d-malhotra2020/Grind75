class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i, current, totalSum):
            if totalSum == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or totalSum > target:
                return
            current.append(candidates[i])
            dfs(i, current, totalSum + candidates[i])
            
            current.pop()
            dfs(i+1, current, totalSum)
            
        dfs(0, [], 0)
        return result
            
        