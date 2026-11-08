class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]

        for u, v, time in times:
            adj[u].append((time, v))

        heap = [(0,k)]
        seen = set()

        while heap:
            delay, node = heapq.heappop(heap)
            
            if node in seen:
                continue

            seen.add(node)

            totalTime = delay
            for time, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(heap, (totalTime + time, nei))

        return totalTime if len(seen) == n else -1
            