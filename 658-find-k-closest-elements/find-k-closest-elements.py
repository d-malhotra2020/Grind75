class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for n in arr:
            distance = abs(n - x)
            if len(heap) < k:
                heapq.heappush(heap, (-distance, n))
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, (-distance, n))
        distances = [p[1] for p in heap]
        distances.sort()
        return distances