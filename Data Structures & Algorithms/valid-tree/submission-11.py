class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        if len(edges) != n-1:
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()

        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for nei in adj[node]:
                dfs(nei)

        dfs(0)
        return len(seen) == n