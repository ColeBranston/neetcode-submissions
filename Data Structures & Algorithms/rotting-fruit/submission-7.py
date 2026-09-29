class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        length = len(grid)
        width = len(grid[0])
        q = deque()
        seen = set()
        total = 0

        for i in range(length):
            for j in range(width):
                if grid[i][j] == 2:
                    q.append((i,j))

                elif grid[i][j] == 1:
                    total += 1

            print(grid[i])

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()

                if not 0 <= i < length or not 0 <= j < width or (i,j) in seen:
                    continue

                seen.add((i,j))

                if grid[i][j] == 1:
                    total -= 1
                    grid[i][j] = 2

                if total == 0:
                    return res

                for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0 <= x < length and 0 <= y < width and (x,y) not in seen and grid[x][y] == 1:
                        q.append((x,y))

            res += 1

        return res if not total else -1