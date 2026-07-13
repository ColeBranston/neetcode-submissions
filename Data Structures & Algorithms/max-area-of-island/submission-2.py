class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = set()

        maxx = 0

        def countIslands(i, j):
            nonlocal visited

            if not 0 <= i < height or not 0 <= j < width or grid[i][j] == 0 or (i,j) in visited:
                return 0

            visited.add((i,j))
            sizeCounts = 0
            for x,y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                sizeCounts += countIslands(x,y)

            return 1 + sizeCounts

        for i in range(height):
            for j in range(width):
                maxx = max(maxx, countIslands(i,j))

        return maxx