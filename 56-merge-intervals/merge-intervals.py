class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        alreadyMerged = []
        intervals.sort(key = lambda x: x[0])
        for i in intervals:
          if not alreadyMerged or i[0] > alreadyMerged[-1][1]:
            alreadyMerged.append(i)
          else:
            alreadyMerged[-1][1] = max(alreadyMerged[-1][1], i[1])
        return alreadyMerged