class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        placed = False

        for interval in intervals:
            a0, a1 = interval
            b0, b1 = newInterval

            if a1 < b0:
                # entirely to the left
                res.append(interval)
            elif a0 <= b0 <= a1 or b0 <= a0 <= b1:
                # overlap: one of them starts inside the other
                newInterval = [min(a0, b0), max(a1, b1)]
            else:
                # entirely to the right
                if not placed:
                    res.append(newInterval)
                    placed = True
                res.append(interval)

        if not placed:
            res.append(newInterval)

        return res