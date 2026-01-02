from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        prereqCount = [0] * numCourses

        for a, b in prerequisites:
          graph[b].append(a)
          prereqCount[a] += 1

        queue = deque()
        for i in range(numCourses):
          if prereqCount[i] == 0:
            queue.append(i)
        
        order = []
        while queue:
          course = queue.popleft()
          order.append(course)
          for neighbor in graph[course]:
            prereqCount[neighbor] -= 1
            if prereqCount[neighbor] == 0:
              queue.append(neighbor)

        return order if len(order) == numCourses else []


