# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        tail = dummy
        first = head

        while first and first.next:
            second = first.next


            tail.next = second
            first.next = second.next
            second.next = first

            tail = first
            first = first.next
        return dummy.next 