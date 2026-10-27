class Solution:
    def euclidianSortKey(self, item: List[int]) -> int:
        return (item[0])**2 + (item[1])**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = self.euclidianSortKey)

        return points[0:k]

        