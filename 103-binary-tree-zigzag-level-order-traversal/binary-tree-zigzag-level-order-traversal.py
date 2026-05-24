# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        left_to_right = True
        result = []

        while queue:
            level = len(queue)
            node_to_level = deque()
            for i in range(level):
                node = queue.popleft()
                if left_to_right:
                    node_to_level.append(node.val)
                else:
                    node_to_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(node_to_level))
            left_to_right = not left_to_right
        return result

            


