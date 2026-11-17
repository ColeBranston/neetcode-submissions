class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1

        selected = None

        while l <= r:
            n = (l+r) // 2

            if target < matrix[n][0]:
                r = n-1

            elif target > matrix[n][-1]:
                l = n+1

            else:
                selected = matrix[n]
                break

        if not selected:
            return False

        l,r = 0,len(selected)-1

        while l <= r:
            n = (l+r) // 2

            if target < selected[n]:
                r = n-1

            elif target > selected[n]:
                l = n+1

            else:
                return True

        return False