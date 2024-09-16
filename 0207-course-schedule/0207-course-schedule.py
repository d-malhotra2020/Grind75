class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashmap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            hashmap[course].append(pre)
            
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if hashmap[course] == []:
                return True
            
            visit.add(course)
            for pre in hashmap[course]:
                if not dfs(pre): 
                    return False
                
            visit.remove(course)
            hashmap[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
                    