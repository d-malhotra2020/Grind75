class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)

            elif n > heap[0]:
                heapq.heappushpop(heap, n)
        return heap[0]