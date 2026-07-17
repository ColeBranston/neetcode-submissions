class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        '''
        Basically approach the problem with the queston of how can I get to the pacific or atlantic from here?
        For the desired ocean, you start from either set of sides ie. top, left or bottom, right, respectively,
        and call the dfs function to add to the ocean's visited set if the current height is >= to the previous
        and it hasn't been seen before to avoid cycles + infinite recursion. This involves a for loop, calling
        the dfs function for indexes of the left and right sides for pacific and atlantic, and a second for loop
        including the indexes for the top and bottom, pacific and atlantic, respectively. Finally with both visited
        sets built, therefore including all paths to the pacific and atlantic oceans, a final double nested for
        loop itterates through each node on the graph and checks whether that i,j index is apart of a path in
        both visited sets. If it is, the i,j index is added to the final output. After finalizing all different
        nodes the res is returned and Boom you've solved the question.
        '''
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
