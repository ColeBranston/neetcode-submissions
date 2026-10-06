class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cycle = set()
        seen = set()

        def dfs(node):
            if node in cycle:
                return False

            if node in seen:
                return True

            cycle.add(node)

            for nei in adj[node]:
                dfs(nei)

            cycle.remove(node)
            seen.add(node)
            return True

        res = 0

        for i in range(n):
            if i not in seen:
                res += 1
                dfs(i)

        return res


