class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        The goal of this question is simply to understand dfs and birdirectional traversals similar
        to isTree. This means you make a bidirectional adjacency matrix, then you use a visited set
        to check and each node, then use the adjacency matrix to add more nodes that are connected.
        Then at the end all you have to do is check if the current node is init visit, and if its not,
        add to the counter, and call the dfs method on that node clearinig any connected nodes
        '''

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)

            for nei in adj[node]:
                dfs(nei)
        count = 0
        for node in range(n):
            if node not in visit:
                count += 1
                dfs(node)

        return count
