# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev_node = None
        curr_node = slow

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
        
        first = head
        second = prev_node

        while second.next:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        return head