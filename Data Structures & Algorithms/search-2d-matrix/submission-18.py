class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1,r1 = 0, len(matrix)-1

        if not matrix:
            return False

        targetMatrix = None

        while l1 <= r1:
            n = (l1+r1) // 2
            nLength = len(matrix[n])

            if matrix[n][0] <= target <= matrix[n][nLength-1]:
                targetMatrix = matrix[n]
                break

            elif target < matrix[n][0]:
                r1 = n-1

            elif target > matrix[n][nLength-1]:
                l1 = n+1

        if not targetMatrix: 
            return False

        l2,r2 = 0,len(targetMatrix)-1
        print(targetMatrix)
        print(l2,r2)

        while l2 <= r2:
            n = (l2+r2)//2

            if target < targetMatrix[n]:
                r2 = n-1

            elif target > targetMatrix[n]:
                l2 = n+1

            elif target == targetMatrix[n]:
                return True

        return False
        