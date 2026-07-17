class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        '''
        Basically works the same way as pacifc and atlantic but easier as you can run the same 
        method for a ring around the grid. Logically anything that is unreachable from the edges
        is encased in X's if we only traverse O's. So we run the same method that instead of adding to a
        set, simply marks the spot as T for visited and continues, therefore removing cycle errors. You
        then smply run two for loops, one for loop for the first and last column, and the second for loop
        for the first and last row. This ensures that all O's reachable from the edge become T's. Finally, 
        a doubly nested for loop runs through and turns all T's back to O's and all O's to X's as those
        remaining O's were untouched and therefore unreachable and encased.
        '''

        def capture(i, j):
            if not 0 <= i < ROWS or not 0 <= j < COLS or board[i][j] != "O":
                return

            board[i][j] = "T"
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                capture(x,y)

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"