class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        The goal of this approach is to create a bidirectional adjacency matrix
        done through adding each node to eachothers matrix nodes, then we simply check against 
        a visited set, and pass in the current node to the next call

        we should also check that the number of edges is equal to the number of nodes - 1
        '''

        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        return dfs(0,-1) and len(visit) == n
