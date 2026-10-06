class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        if len(edges) != n-1:
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cycle = set()
        seen = set()

        def dfs(node):
            if node in cycle:
                return True

            if node in seen:
                return False

            cycle.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            cycle.remove(node)
            seen.add(node)
            return True

        dfs(0)
        return len(seen) == n