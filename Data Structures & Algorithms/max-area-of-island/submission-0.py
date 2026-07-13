class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        height = len(grid)
        width = len(grid[0])

        def countIslands(i, j, count):
            if grid[i][j] == "#":
                return count

            if grid[i][j] == 1:
                count += 1
                grid[i][j] = "#"

                for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= x < height and 0 <= y < width:
                        count = countIslands(x, y, count)

            return count

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    maxx = max(maxx, countIslands(i, j, 0))

        return maxx