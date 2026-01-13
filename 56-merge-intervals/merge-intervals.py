class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda x: x[0])
        for i in intervals:
          if not merged or i[0] > merged[-1][1]:
            merged.append(i)
          else:
            merged[-1][1] = max(merged[-1][1], i[-1])
        return merged