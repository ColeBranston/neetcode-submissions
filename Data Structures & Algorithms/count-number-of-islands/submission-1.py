class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        height = len(grid)
        width = len(grid[0])

        def countIslands(i,j):
            if grid[i][j] == '1':
                grid[i][j] = '#'

                for x,y in ((i+1, j),(i-1, j),(i,j+1),(i,j-1)):
                    if 0 <= x < height and 0 <= y < width:
                        countIslands(x,y)

                return True

            return False

        count = 0
        for i in range(height):
            for j in range(width):
                if countIslands(i, j):
                    count += 1

        return count

