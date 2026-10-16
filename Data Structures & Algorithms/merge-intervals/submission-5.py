class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key = lambda x: x[0])

        i = 1
        prev = intervals[0]
        placed = False
        while i < len(intervals):
            if prev[0] <= intervals[i][0] <= prev[1] or prev[0] <= intervals[i][1] <= prev[1]:
                prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])

            else:
                if not placed:
                    res.append(prev)
                    placed = True

                res.append(intervals[i])
                prev = intervals[i]
            
            i += 1

        return res if res else [prev]

            