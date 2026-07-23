class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        # visit = [False] * (n+1) ## another form of visited tracking

        def dfs(node, par):
            if visit[node]:
                return False

            visit[node] = True

            for nei in adj[node]:
                if nei == par:
                    continue
                
                if not dfs(nei, node):
                    return False

            return True

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visit = [False] * (n+1)

            if not dfs(u, -1):
                return [u,v]

        return []
