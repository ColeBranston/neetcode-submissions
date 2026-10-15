from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            best = 1                      # nums[i] by itself
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
            return best

        return max(dfs(i) for i in range(len(nums)))