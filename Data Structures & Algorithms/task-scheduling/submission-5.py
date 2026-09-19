class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1

        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]

            else:
                count = 1 + heapq.heappop(maxHeap)
                if count: 
                    q.append([count, time + n])

            if q and q[0][1] == time:
                count = q.popleft()[0]
                heapq.heappush(maxHeap, count)

        return time

            

