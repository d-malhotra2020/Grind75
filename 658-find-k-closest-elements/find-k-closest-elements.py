class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for a in arr:
            distance = abs(a - x)
            if len(heap) < k:
                heapq.heappush(heap, (-distance, a))
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, (-distance, a))
        distances = [p[1] for p in heap]
        distances.sort()
        return distances