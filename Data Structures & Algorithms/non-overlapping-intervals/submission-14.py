class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0

        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prevEnd > curr[0]:
                count += 1

            else:
                prevEnd = curr[1]

        return count