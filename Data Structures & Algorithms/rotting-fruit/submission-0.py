class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visit = set()

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
                if 0 <= i < height and 0 <= j < weight and (i,j) not in visit and grid[i][j] != 0:
                    print("Current passed gate: ", i,",",j)
                    
                    visit.add((i,j))
                    
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        print(f'Decrementing numFresh, prev: {numFresh}, new: {numFresh-1}')
                        numFresh -= 1

                    if numFresh == 0:
                        return output

                    for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        q.append((x,y))

                    print("increasing count, new count: ", output)

            output += 1

        return output if numFresh == 0 else -1