"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

      merged = []
      flat = []
      free_time = []

      for employee in schedule:
        for interval in employee:
          flat.append(interval)
      flat.sort(key = lambda x: x.start)

      for i in flat:
        if not merged or i.start > merged[-1].end:
          merged.append(i)
        else:
          merged[-1].end = max(i.end, merged[-1].end)

      for j in range(1, len(merged)):
        start = merged[j-1].end
        end = merged[j].start
        if start < end:
          free_time.append(Interval(start, end))
      return free_time

        




          

