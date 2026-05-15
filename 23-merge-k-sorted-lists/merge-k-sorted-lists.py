# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        nonEmpty = []
        
        for head in lists:
            if head:
                nonEmpty.append(head)

        if not nonEmpty:
            return None
        
        for head in nonEmpty:
            heapq.heappush(heap, (head.val, id(head), head))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node), node.next))
        return dummy.next

        
        