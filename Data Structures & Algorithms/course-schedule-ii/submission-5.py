class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        currCycle = set()
        seen = set()

        topo_order = []

        def dfs(node):
            if node in currCycle:
                return False
            if node in seen:
                return True

            currCycle.add(node)

            for course in adj[node]:
                if not dfs(course):
                    return False

            currCycle.remove(node)
            seen.add(node)

            topo_order.append(node)

            return True

        for courseId in range(numCourses):
            if not dfs(courseId):
                return []

        return topo_order[::-1]