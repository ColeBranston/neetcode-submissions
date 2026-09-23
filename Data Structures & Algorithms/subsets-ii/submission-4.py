class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(curr, index):
            nonlocal res
           
            res.append(curr.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()

        backtrack([], 0)
        return res