class MedianFinder:

    def __init__(self):
        self.leftMax = []
        self.rightMin = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftMax, -num)
        
        if len(self.rightMin) < len(self.leftMax):
            heapq.heappush(self.rightMin, -heapq.heappop(self.leftMax))

        if self.leftMax and self.rightMin[0] < -self.leftMax[0]:
            heapq.heappush(self.leftMax, -heapq.heappop(self.rightMin))
            heapq.heappush(self.rightMin, -heapq.heappop(self.leftMax))

    def findMedian(self) -> float:
        if len(self.rightMin) > len(self.leftMax):
            return self.rightMin[0]

        return (-self.leftMax[0] + self.rightMin[0]) / 2
        