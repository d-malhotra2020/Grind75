# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(current, previous):
            if current is None:
                return previous
            else:
                next = current.next
                current.next = previous
                return reverse(next,current)
        return reverse(head,None)