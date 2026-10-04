class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(i,j, prevHeight, ocean):
            if not 0 <= i < rows or not 0 <= j < cols or (i,j) in ocean or heights[i][j] < prevHeight:
                return

            ocean.add((i,j))

            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                dfs(x,y, heights[i][j], ocean)

        atlantic = set()
        pacific = set()
        for i in range(rows):
            dfs(i, 0, float('-inf'), pacific)
            dfs(i, cols-1, float('-inf'), atlantic)

        for j in range(cols):
            dfs(0, j, float('-inf'), pacific)
            dfs(rows-1, j, float('-inf'), atlantic)

        res = []
        for tup in atlantic:
            if tup in pacific:
                res.append(list(tup))

        return res
