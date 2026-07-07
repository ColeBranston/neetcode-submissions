"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        res = []

        for i in intervals:
            if res and res[0] <= i.start:
                heapq.heappop(res)

            heapq.heappush(res, i.end)
        
        return len(res)