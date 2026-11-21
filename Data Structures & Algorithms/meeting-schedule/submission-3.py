"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals = [[x.start, x.end] for x in intervals]
        intervals.sort()
        
        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]
            curr_start = intervals[i][0]
            
            if curr_start < prev_end:
                return False
                
        return True
