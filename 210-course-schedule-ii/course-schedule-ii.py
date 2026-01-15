from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        prerequisiteCount = [0] * numCourses

        for a, b in prerequisites:
          graph[b].append(a)
          prerequisiteCount[a] += 1

        queue = deque()
        for i in range(numCourses):
          if prerequisiteCount[i] == 0:
            queue.append(i)

        order = []
        while queue:
          course = queue.popleft()
          order.append(course)
          for neighbor in graph[course]:
            prerequisiteCount[neighbor] -= 1
            if prerequisiteCount[neighbor] == 0:
              queue.append(neighbor)
        return order if len(order) == numCourses else []
          
            
          
        