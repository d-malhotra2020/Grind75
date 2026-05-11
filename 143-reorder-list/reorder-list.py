# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = None
        current = slow

        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode

        first = head
        second = prev

        while second.next:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            first = first_next

            second.next = first
            second = second_next
        
        return head
        
