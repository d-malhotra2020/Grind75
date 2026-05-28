class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        busStop = {}
        
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in busStop:
                    busStop[stop] = []
                busStop[stop].append(i)
        
        visited = set()
        queue = deque()

        if source not in busStop:
            return -1

        for bus in busStop[source]:
            queue.append((bus, 1))
            visited.add((bus))
        
        while queue:
            currentBus, numChanges = queue.popleft()
            
            for stop in routes[currentBus]:
                if stop == target:
                    return numChanges
            
                for busConnection in busStop[stop]:
                    if busConnection not in visited:
                        queue.append((busConnection, numChanges + 1))
                        visited.add((busConnection))
        return -1
        
