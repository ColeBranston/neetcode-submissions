class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        weight = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i,j, visit, previous):
            if (i,j) in visit or not 0 <= i < height or not 0 <= j < weight or heights[i][j] < previous:
                return None

            visit.add((i,j))
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                dfs(x,y,visit,heights[i][j])

        for i in range(height):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, weight-1, atlantic, heights[i][weight-1])

        for i in range(weight):
            dfs(0, i, pacific, heights[0][i])
            dfs(height-1, i, atlantic, heights[height-1][i])

        res = []
        for i in range(height):
            for j in range(weight):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])

        return res
