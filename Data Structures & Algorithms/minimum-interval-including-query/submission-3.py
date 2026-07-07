class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        i = 0
        res = {}
        intervals.sort(key=lambda x: x[0])

        for q in sorted(queries): # this ensures that every query after the current is greater than so the correct interval will always be at the current index or in the next set of indexs, but we never need to go back
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i+=1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]

            