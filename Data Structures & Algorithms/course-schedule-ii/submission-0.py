class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[b].append(a)

        visit = set()
        seen = set()

        topo_order = []

        def dfs(node):
            if node in visit:
                return False
                
            if node in seen:
                return True

            visit.add(node)

            for nextt in adj[node]:
                if not dfs(nextt):
                    return False
            
            visit.remove(node)
            seen.add(node)
            topo_order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return topo_order[::-1]