class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(x, y, i):
            if i == len(word):
                return True
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS or
                word[i] != board[x][y] or board[x][y] == '#'):
                return False

            board[x][y] = '#'
            res = (dfs(x + 1, y, i + 1) or
                   dfs(x - 1, y, i + 1) or
                   dfs(x, y + 1, i + 1) or
                   dfs(x, y - 1, i + 1))
            board[x][y] = word[i]
            return res

        for x in range(ROWS):
            for y in range(COLS):
                if dfs(x, y, 0):
                    return True
        return False