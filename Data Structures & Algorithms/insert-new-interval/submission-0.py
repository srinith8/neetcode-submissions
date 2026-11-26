class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[intervals[0]]
        for start, end in intervals[1:]:
            last_end=res[-1][1]
            if start<=last_end:
                res[-1][1]=max(last_end,end)
            else:
                res.append([start,end])
        return res
        