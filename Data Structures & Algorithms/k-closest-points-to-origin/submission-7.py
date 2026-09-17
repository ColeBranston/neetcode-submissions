class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            heapq.heappush(heap, [-(point[0]**2 + point[1]**2),point])
            while len(heap) > k:
                heapq.heappop(heap)

        return [point for val, point in heap]