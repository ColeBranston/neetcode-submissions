class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, time in times:
            adj[u].append((time, v))

        heap = [(0, k)]
        seen = set()

        while heap:
            time, node = heapq.heappop(heap)

            if node in seen:
                continue

            seen.add(node)
            totalTime = time
            for neiTime, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(heap, (neiTime + time, nei))

        return totalTime if len(seen) == n else -1