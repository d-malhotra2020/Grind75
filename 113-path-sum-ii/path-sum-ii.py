# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, target, path):

            if not node:
                return 0
                
            path.append(node.val)
            if not node.left and not node.right:
                if target == node.val:
                    result.append(path[:])
            
            dfs(node.left, target - node.val, path)
            dfs(node.right, target - node.val, path)
            
            path.pop()

        

        
        result = []
        dfs(root, targetSum, [])
        return result



