class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index, curr):
            nonlocal res

            res.append(curr.copy())

            for j in range(index, len(nums)):
                if j > index and nums[j] == nums[j-1]:
                    continue

                curr.append(nums[j])
                dfs(j+1, curr)
                curr.pop()
                

        dfs(0, [])
        return res