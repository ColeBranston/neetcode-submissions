class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []

        i = 0

        '''
        Three check method where we cover first the intervals completely excluded, 
        second the overlapping intervals, and then finally everything else
        '''
        
        '''
        checks for all intervals before the new interval checking the 
        end time of curr is < than the start of the new 
        '''
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i+=1

        '''
        based on the previous check we know that the start time of the new interval is less than or equal
        to the end time of the current interval, therefore the start time is inside the interval

        + we also check if the end time of the new interval is greater than or equal to the start time
        of the current interval



        '''
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i+=1

        return res