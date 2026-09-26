class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length = len(grid)
        width = len(grid[0])
        count = 0

        def dfs(i,j):
            if not 0 <= i < length or not 0 <= j < width or grid[i][j] != "1":
                return

            grid[i][j] = "#"
            
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                dfs(x,y)

        for i in range(length):
            for j in range(width):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)

        return count