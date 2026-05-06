class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      
      count = 1
      intervals.sort(key = lambda x:x[1])
      right = intervals[0][1]

      for i in range(len(intervals)):
        if right <= intervals[i][0]:
          right = intervals[i][1]
          count += 1
      return len(intervals) - count