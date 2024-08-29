class Solution:
    def mergeIntervals(self, intervals):
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        merged = []
                
        for interval in sortedIntervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged