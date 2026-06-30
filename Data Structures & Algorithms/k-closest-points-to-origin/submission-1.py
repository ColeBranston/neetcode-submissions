class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(point):
            x = point[0]
            y = point[1]

            return math.sqrt(((0-x)**2 + (abs(0-y)**2)))

        heap = [(calcDistance(point),(point[0], point[1])) for point in points]

        heapq.heapify(heap)

        output = []
        for distance, point in heapq.nsmallest(k, heap):
            output.append(point)

        return output