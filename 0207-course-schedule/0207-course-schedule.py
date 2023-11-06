class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}
        
        for courses, prereqs in prerequisites:
            preMap[courses].append(prereqs)
            
        visitSet = set()
        def dfs(courses):
            if courses in visitSet:
                return False
            if preMap[courses] == []:
                return True
            
            visitSet.add(courses)
            for prereqs in preMap[courses]:
                if not dfs(prereqs):
                    return False
            visitSet.remove(courses)
            preMap[courses] = []
            return True
        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True