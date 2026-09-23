class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def backtrack(curr, index):
            nonlocal res
           
            if tuple(curr.copy()) not in res:
                res.add(tuple(curr.copy()))

            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()

        backtrack([], 0)
        return [list(tup) for tup in res]