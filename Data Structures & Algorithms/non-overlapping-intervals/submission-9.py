class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        '''
        extremely elegant solution where after you've sorted
        you know that the curr intervals end is after the prev end as you've
        sorted by the end time, therefore all you need to check for is that the 
        prev end is > than the start that way you know that the overlap is when
        curr_start < prev_end < curr_end signifying an overlap
        '''
        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]

        return res