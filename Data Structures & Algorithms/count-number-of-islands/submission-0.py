class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        height = len(grid)-1
        width = len(grid[0])-1

        def printGrid(grid):
            for i in range(len(grid)):
                print(grid[i])
            
            print()

        def countIslands(i,j):
            printGrid(grid)
            if grid[i][j] == '1':
                print("Detected 1: ", grid[i][j])
                grid[i][j] = '#'

                for x,y in ((i+1, j),(i-1, j),(i,j+1),(i,j-1)):
                    if 0 <= x <= height and 0 <= y <= width:
                        countIslands(x,y)

                return True

            return False

        count = 0
        for i in range(height+1):
            for j in range(width+1):
                print("Current Index: ", f'grid[{i}][{j}]: {grid[i][j]}')
                if countIslands(i, j):
                    count += 1

        return count

