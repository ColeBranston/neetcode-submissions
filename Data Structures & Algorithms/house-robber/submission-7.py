class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        cache = {}
        def dfs(i):
            if i >= length:
                return 0

            if i in cache:
                return cache[i]

            cache[i] = max(dfs(i+1), nums[i] + dfs(i+2))

            return cache[i]

        return dfs(0)