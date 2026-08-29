class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = set()
        adj = defaultdict(list)

        for u, v, time in times:
            adj[u].append((time, v))

        heap = [(0, k)]
        wt = 0
        print(adj)
        while heap:
            time1, node = heapq.heappop(heap)
            if node in seen:
                continue

            seen.add(node)
            wt = time1

            for time2, n2 in adj[node]:
                if n2 not in seen:
                    heapq.heappush(heap, (time1 + time2, n2))
        
        print(seen)
        return wt if len(seen) == n else -1

