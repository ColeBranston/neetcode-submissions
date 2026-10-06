class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = []

        res = []
        adj = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[u].append(v)

        cycle = set()
        seen = set()

        def dfs(node):
            nonlocal res

            if node in cycle:
                return False

            if node in seen:
                return True

            cycle.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            cycle.remove(node)
            seen.add(node)
            res.append(node)
            return True

        for course in range(numCourses):
            dfs(course)

        return res if len(res) == numCourses else []