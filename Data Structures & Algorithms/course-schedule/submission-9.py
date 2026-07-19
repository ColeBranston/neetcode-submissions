class Solution:
   def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       adj = [[] for _ in range(numCourses)]
       for a, b in prerequisites:
           adj[b].append(a)

       topo_order = []
       visited = set()
       def dfs(node):
           if node in visited:
               return False
           visited.add(node)
           for nei in adj[node]:
               if not dfs(nei):
                   return False
           visited.remove(node)
           topo_order.append(node)
           return True
       for i in range(numCourses):
           if not dfs(i):
               return False
       return True