class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRow(row):
            for num in row:
                if num != "." and row.count(num) > 1:
                    return False
            return True  # <-- FIXED: moved outside the loop to avoid early return


        def checkCol(board):
            for i in range(9):
                # <-- FIXED: simplified column construction
                col = [board[j][i] for j in range(9)]
                if not checkRow(col):  # <-- FIXED: changed from `checkRow(col) == False` to Pythonic form
                    return False
            return True


        def checkBox(board):
            for box_row in range(3):
                for box_col in range(3):
                    box = []
                    for i in range(3):
                        for j in range(3):
                            # <-- FIXED: simplified box traversal
                            box.append(board[box_row * 3 + i][box_col * 3 + j])
                    if not checkRow(box):  # <-- FIXED
                        return False
            return True


        # Check rows
        for i in range(len(board)):
            if not checkRow(board[i]):  # <-- FIXED: changed from `checkRow(...) == False`
                print("Row", i, "→ False")
                return False
            else:
                print("Row", i, "→ True")

        # Check columns
        if not checkCol(board):  # <-- FIXED: changed from `if checkCol == False:`
            print("Column Check → False")
            return False
        else:
            print("Column Check → True")

        # Check boxes
        if not checkBox(board):  # <-- FIXED: changed from `if checkBox(board) == False:`
            print("Box Check → False")
            return False
        else:
            print("Box Check → True")

        return True