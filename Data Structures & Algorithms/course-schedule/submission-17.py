class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[v].append(u)

        visit = set()
        seen = set()

        def dfs(node):
            if node in visit:
                return False

            if node in seen:
                return True
            
            visit.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visit.remove(node)
            seen.add(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
