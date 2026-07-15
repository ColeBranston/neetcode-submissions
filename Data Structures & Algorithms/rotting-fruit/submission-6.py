class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        height = len(grid)
        weight = len(grid[0])

        numFresh = 0
        output = 0

        for i in range(height):
            for j in range(weight):
                if grid[i][j] == 2:
                    q.append([i,j])

                if grid[i][j] == 1:
                    numFresh += 1
        
        while q:
            length = len(q)
            for _ in range(length):
                i,j = q.popleft()
                
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    numFresh -= 1

                if numFresh == 0:
                    return output

                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= x < height and 0 <= y < weight and grid[x][y] == 1: 
                        q.append((x,y))

            output += 1

        return output if numFresh == 0 else -1