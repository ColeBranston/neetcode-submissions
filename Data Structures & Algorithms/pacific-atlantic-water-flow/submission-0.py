class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        output = []

        def dfs(r, c, visited, pacific):
            # Reached the correct ocean
            if pacific:
                if r == 0 or c == 0:
                    return True
            else:
                if r == rows - 1 or c == cols - 1:
                    return True

            visited.add((r, c))

            for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] <= heights[r][c]
                ):
                    if dfs(nr, nc, visited, pacific):
                        return True

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, set(), True) and dfs(r, c, set(), False):
                    output.append([r, c])

        return output