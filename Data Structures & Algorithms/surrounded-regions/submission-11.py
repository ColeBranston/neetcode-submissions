class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def safe(i,j):
            if not 0 <= i < rows or not 0 <= j < cols or board[i][j] != 'O':
                return

            board[i][j] = 'T'

            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                safe(x,y) 


        for i in range(rows):
            if board[i][0] == 'O':
                safe(i,0)
            if board[i][cols-1] == "O":
                safe(i,cols-1)

        for j in range(cols):
            if board[0][j] == "O":
                safe(0,j)
            if board[rows-1][j] == "O":
                safe(rows-1,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        