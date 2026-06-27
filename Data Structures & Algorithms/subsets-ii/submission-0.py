class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        check = set()

        for i in range(len(nums)):
            temp = []
            for j in range(len(res)):
                newArray = [nums[i]] + res[j]
                checkArray = sorted(newArray)
                if tuple(checkArray) not in check:
                    check.add(tuple(checkArray))
                    temp.append(newArray)

            res += temp

        return res