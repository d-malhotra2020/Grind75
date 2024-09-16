class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashmap = {i:[] for i in range(numCourses)}
        for courses, prereqs in prerequisites:
            hashmap[courses].append(prereqs)
            
        visit = set()
        
        def dfs(courses):
            if courses in visit:
                return False
            if hashmap[courses] == []:
                return True
            
            visit.add(courses)
            for prereqs in hashmap[courses]:
                if not dfs(prereqs):
                    return False
            visit.remove(courses)
            hashmap[courses] = []
            return True
            
        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True
                
                
            
        