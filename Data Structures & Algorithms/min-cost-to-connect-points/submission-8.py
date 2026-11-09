class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        matrix = []

        if not points:
            return 0

        counter = 1
        mapp = {}

        for point in points:
            mapp[tuple(point)] = counter
            counter += 1

        for i in range(len(points)):
            for j in range(i, len(points)):
                p1 = tuple(points[i])
                p2 = tuple(points[j])

                weight = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

                matrix.append((mapp[p1], mapp[p2], weight))

        adj = defaultdict(list)

        for u,v,weight in matrix:
            adj[u].append((weight, v))
            adj[v].append((weight, u))
        
        heap = [(0, 1)]
        seen = set()
        total = 0

        while heap:
            weight, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            total += weight                      # accumulate edge cost

            for neiWeight, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(heap, (neiWeight, nei))   # edge weight only

        return total







            