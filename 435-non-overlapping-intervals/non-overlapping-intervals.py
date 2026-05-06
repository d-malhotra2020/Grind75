class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      
      intervals.sort(key = lambda x:x[1])
      right = intervals[0][1]
      count = 1

      for i in range(len(intervals)):
        if right <= intervals[i][0]:
          right = intervals[i][1]
          count += 1
      return 0 if not intervals else (len(intervals) - count)
    

      
        