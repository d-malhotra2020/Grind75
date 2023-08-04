"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None: None}
        current = head
        while current:
            copy = Node(current.val)
            oldtocopy[current] = copy
            current = current.next
        current = head
        while current:
            copy = oldtocopy[current]
            copy.next = oldtocopy[current.next]
            copy.random = oldtocopy[current.random]
            current = current.next
        return oldtocopy[head]