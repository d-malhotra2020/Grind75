class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}
        visit = set()
        
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        
        def dfs(course):
            if course in visit:
                return False
            if hashmap[course] == []:
                return True
            visit.add(course)
            
            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            hashmap[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True