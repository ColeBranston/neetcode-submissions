class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        '''
        DFS Topological sort O(V+E) for space and time where V = Verticie and E = Edge
        '''
        
        adj = [[] for _ in range(numCourses)]

        for reqCourse, prereq in prerequisites:
            adj[prereq].append(reqCourse)

        currCycle = set()
        seen = set()

        def dfs(node):
            if node in currCycle:
                return False
            if node in seen:
                return True

            currCycle.add(node)

            for reqCourse in adj[node]:
                if not dfs(reqCourse):
                    return False

            currCycle.remove(node)
            seen.add(node)

            return True

        for course in range(numCourses): # works because each course id is its course count
            if not dfs(course):
                return False

        return True

        