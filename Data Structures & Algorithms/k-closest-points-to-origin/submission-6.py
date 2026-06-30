class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(point):
            x = point[0]
            y = point[1]

            return math.sqrt((x**2 + y**2))

        heap = []
        heapq.heapify(heap)

        for point in points:
            dist = -calcDistance(point)
            
            heapq.heappush(heap, (dist, point))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for dist, point in heap]


            

            
            
