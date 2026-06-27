class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index, curr):
            nonlocal res

            if index == len(nums):
                res.append(curr.copy())
                return

            for j in range(index, len(nums)):
                curr[j], curr[index] = curr[index], curr[j]
                dfs(index+1, curr)
                curr[j], curr[index] = curr[index], curr[j]

        dfs(0, nums)
        return res