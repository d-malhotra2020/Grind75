class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i : [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            premap[course].append(prereq)
            
            #visitSet = all courses along the curr DFS path
            
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if premap[course] == []:
                return True
            visitSet.add(course)
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
            visitSet.remove(course)
            premap[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
                    