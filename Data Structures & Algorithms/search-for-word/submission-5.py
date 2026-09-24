class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS or
                word[index] != board[x][y] or board[x][y] == '#'):
                return False

            board[x][y] = '#'
            res = (dfs(x + 1, y, index + 1) or
                   dfs(x - 1, y, index + 1) or
                   dfs(x, y + 1, index + 1) or
                   dfs(x, y - 1, index + 1))
            board[x][y] = word[index]
            return res

        for x in range(ROWS):
            for y in range(COLS):
                if dfs(x, y, 0):
                    return True
        return False