class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            
        def cycle(node, tracker, visited):
            tracker[node] = True
            visited[node] = True
            
            for n in adjList[node]:
                if n not in visited and cycle(n, tracker, visited):
                    return True
                elif n in tracker:
                    return True
            tracker.pop(node)
            return False
        visited = {}
        for n in range(numCourses):
            tracker = {}
            if n not in visited and cycle(n,tracker, visited):
                return False
        return True