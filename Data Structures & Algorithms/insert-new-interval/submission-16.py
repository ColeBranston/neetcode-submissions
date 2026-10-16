class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        isInserted = False
        nI = newInterval

        for i in intervals:
            if i[1] < nI[0]:
                res.append(i)

            elif i[0] <= nI[0] <= i[1] or i[0] <= nI[1] <= i[1]:
                nI[0] = min(i[0], nI[0])
                nI[1] = max(i[1], nI[1])

            elif i[0] > nI[1]:
                if not isInserted:
                    res.append(nI)
                    isInserted = True

                res.append(i)


        if not isInserted:
            res.append(nI)

        return res