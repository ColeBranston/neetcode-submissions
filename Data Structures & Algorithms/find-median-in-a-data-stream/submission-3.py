class MedianFinder:
    '''
    thoretically you could always split the stream into a minHeap and maxHeap and when the lengths
    are equal simply add the smallest of the minHeap of the left and the largest of the maxHeap to
    the right together
    '''
    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftMaxHeap, -num)
        
        if len(self.leftMaxHeap) - len(self.rightMinHeap) == 2:
            heapq.heappush(self.rightMinHeap, -heapq.heappop(self.leftMaxHeap))

        if self.rightMinHeap and -self.leftMaxHeap[0] > self.rightMinHeap[0]:
            smaller, larger = heapq.heappop(self.rightMinHeap), heapq.heappop(self.leftMaxHeap)
            heapq.heappush(self.rightMinHeap, -larger)
            heapq.heappush(self.leftMaxHeap, -smaller)

        print(self.leftMaxHeap, self.rightMinHeap)

    def findMedian(self) -> float:
        # always take the largest from the max heap if the sizes are unequal

        if len(self.leftMaxHeap) > len(self.rightMinHeap):
            return -self.leftMaxHeap[0]

        else:
            return (-self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2

        print(self.leftMaxHeap, self.rightMinHeap)

        