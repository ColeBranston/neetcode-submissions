class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # maybe do two binary searches

        for array in matrix:
            if target >= array[0] and target <= array[-1]:

                l,r = 0, len(array) - 1

                while l <= r:
                    middle = (l+r) // 2

                    if target < array[middle]:
                        r = middle - 1
                    elif target > array[middle]:
                        l = middle + 1
                    elif target == array[middle]:
                        return True
                        

        return False 