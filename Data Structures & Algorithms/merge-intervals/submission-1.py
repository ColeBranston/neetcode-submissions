class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        I imedietely notice that you should check if the end time is
        greater than or equal to the next end time
        '''

        intervals.sort(key=lambda x: x[0])
        output = []
        i = 0
        last = intervals[i]

        while i < len(intervals):
            curr = intervals[i]
            if last[0] <= curr[0] and last[1] >= curr[0]:
                last[0] = min(last[0], curr[0])
                last[1] = max(last[1], curr[1])
            else:
                output.append(last)
                last = curr

            print(curr, i)

            i+=1
        output.append(last)
        return output
        