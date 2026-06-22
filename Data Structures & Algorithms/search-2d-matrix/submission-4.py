class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # maybe do two binary searches

        l1, r1 = 0, len(matrix) - 1

        flag = True

        while l1 <= r1:
            middle = (l1 + r1) // 2

            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                matrix = matrix[middle]
                flag = False
                break
            elif target > matrix[middle][0] and target > matrix[middle][-1]:
                l1 = middle + 1
            elif target < matrix[middle][0] and target < matrix[middle][-1]:
                r1 = middle - 1

        if flag:
            return False
            
        l2, r2 = 0, len(matrix) - 1

        while l2 <= r2:
            middle2 = (l2 + r2) // 2

            if target > matrix[middle2]:
                l2 = middle2 + 1

            elif target < matrix[middle2]:
                r2 = middle2 - 1

            elif target == matrix[middle2]:
                return True

        return False 