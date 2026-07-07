"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        this is the easiest optimal solution for this problem,

        essentially ...just use a min heap that stores the end times and read from a list of intervals
        sorted by the interval start time, this allows you to assume that the each interval proceeding
        the next interval starts after the previous. This localises the issue to just focus on the whether
        there is a conflict between current meetings and there end times where the size of the minHeap represents
        the number of rooms active
        '''

        intervals.sort(key=lambda x: x.start)
        minHeap = []

        for i in intervals:
            if minHeap and minHeap[0] <= i.start:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, i.end)

        return len(minHeap)