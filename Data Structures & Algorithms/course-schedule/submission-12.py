class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)

        topo_order = []

        visiting = set()   # current DFS path (cycle detection)
        visited = set()    # permanently finished nodes

        def dfs(node):
            # found a cycle
            if node in visiting:
                return False
            # already fully explored this node
            if node in visited:
                return True
            visiting.add(node)
            for nextt in adj[node]:
                if not dfs(nextt):
                    return False

            # finished exploring this node
            visiting.remove(node)
            visited.add(node)

            topo_order.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True