class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            longest = 1

            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if (0 <= x < n and 
                    0 <= y < m and 
                    matrix[x][y] > matrix[i][j]):

                    longest = max(longest, 1 + dfs(x, y))

            cache[(i, j)] = longest
            return longest

        ans = 0

        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))

        return ans