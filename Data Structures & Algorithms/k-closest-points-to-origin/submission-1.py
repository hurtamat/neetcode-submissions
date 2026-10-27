class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for x, y in points:
            dist = x**2 + y**2
            if len(h) < k:
                heapq.heappush(h, (-dist, [x, y]))
            elif -dist > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (-dist, [x, y]))

        retList = []

        for i in h:
            retList.append(i[1])
        
        return retList

        