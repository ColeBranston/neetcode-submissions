class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRow(Array):
            for num in Array:
                if num != "." and Array.count(num) > 1:
                    return False

            return True

        def checkCol(Arrays):

            for i in range(len(Arrays)):
                tempArray = []

                for j in range(len(Arrays[i])):
                    tempArray.append(Arrays[j][i])

                if checkRow(tempArray) == False:
                    return False

            return True


        def checkBox(Arrays):
            stor = {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: [],
                8: [],
                9: []
            }

            for height in range(len(Arrays)):
                for width in range(len(Arrays[height])):
                    if height < 3 and width < 3:
                        stor[1].append(Arrays[height][width])

                    elif height < 3 and 3 <= width < 6:
                        stor[2].append(Arrays[height][width])

                    elif height < 3 and width >= 6:
                        stor[3].append(Arrays[height][width])

                    elif 3 <= height < 6 and width < 3:
                        stor[4].append(Arrays[height][width])

                    elif 3 <= height < 6 and 3 <= width < 6:
                        stor[5].append(Arrays[height][width])

                    elif 3 <= height < 6 and width >= 6:
                        stor[6].append(Arrays[height][width])

                    elif height >= 6 and width < 3:
                        stor[7].append(Arrays[height][width])

                    elif height >= 6 and 3 <= width < 6:
                        stor[8].append(Arrays[height][width])

                    elif height >= 6 and width >= 6:
                        stor[9].append(Arrays[height][width])

            print(list(stor.values()))

            for array in list(stor.values()):
                if not checkRow(array):
                    return False

            return True


        for i in range(len(board)):
            if checkRow(board[i]) == False:
                return False

            else:
                print("True")

        if checkCol(board) == False:
            return False

        else:
            print("True")

        if checkBox(board) == False:
            return False

        else:
            print("True")

        return True

