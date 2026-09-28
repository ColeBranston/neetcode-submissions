class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == INF: # works cause the first one to get there in a non-level order bfs will be the quickest
                    grid[x][y] = grid[i][j] + 1
                    q.append((x, y))