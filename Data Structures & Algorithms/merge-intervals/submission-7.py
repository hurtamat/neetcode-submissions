class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        retInters = []
        intervals.sort()
        n = len(intervals)
        if not intervals:
            return []
        if n == 1:
            return intervals

        i = 0
        while i < n:
            if i == n - 1:
                retInters.append(intervals[i])
                break
            if intervals[i][1] < intervals[i+1][0]:
                retInters.append(intervals[i])
                i+= 1
                continue
            newInt = intervals[i]
            while i < n - 1 and newInt[1] >= intervals[i+1][0]:
                newInt[1] = max(intervals[i+1][1], newInt[1])
                i+= 1
            retInters.append(newInt)
            i+= 1

        return retInters


        



