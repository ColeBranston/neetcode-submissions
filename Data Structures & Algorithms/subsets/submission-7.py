class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            temp = []

            for array in res:
                temp.append(array + [num])

            res += temp
        
        return res