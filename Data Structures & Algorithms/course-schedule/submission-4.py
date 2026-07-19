class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[b].append(a) # you must go to indice b before a

        topo_order = []
        visit = set()

        def dfs(node):
            if node in visit:
                return False

            visit.add(node)

            for nextt in adj[node]: # go to every course after this prereq
                if not dfs(nextt):
                    return False # if there is a cycle detection later down the chain, continue it up the chain

            visit.remove(node)
            topo_order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True