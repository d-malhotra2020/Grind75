# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        totalMax = 0

        while queue:
            level = len(queue)
            _, leftPos = queue[0]
            rightPos = -1

            for i in range(level):
                node, pos = queue.popleft()
                if i == level - 1:
                    rightPos = pos
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
            totalMax = max(totalMax, rightPos - leftPos + 1)
        return totalMax