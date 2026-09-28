class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy          # register before recursing so cycles resolve
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None