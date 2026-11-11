import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        res = []
        rows = len(points)

        for i in range(rows):
            d[i] = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        sorted_d = dict(sorted(d.items(),key=lambda item: item[1]))

        for _ in range(0, k):
            key = next(iter(sorted_d))
            node = sorted_d.pop(key)
            res.append(points[key])

        return res