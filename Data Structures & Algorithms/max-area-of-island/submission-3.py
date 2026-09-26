class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        length = len(grid)
        width = len(grid[0])

        def dfs(i,j):
            if not 0 <= i < length or not 0 <= j < width or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            count = 1
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                count += dfs(x,y)

            return count

        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    maxx = max(dfs(i,j), maxx)

        return maxx