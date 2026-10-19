"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Time: O(nlogn)
        # Space: O(1)
        intervals.sort(key=lambda x: x.end)
        for i in range(len(intervals)):
            if i and intervals[i-1].end > intervals[i].start:
                return False 

        return True