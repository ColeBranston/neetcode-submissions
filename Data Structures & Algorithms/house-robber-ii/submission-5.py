class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        cache = {
            True: {},
            False: {}
        }
        def dfs(i, isFirst):
            if i >= length:
                return 0

            if i == length - 1 and isFirst:
                return 0

            if i in cache[isFirst]:
                return cache[isFirst][i]

            cache[isFirst][i] = max(dfs(i+1, isFirst), nums[i] + dfs(i+2, isFirst))

            return cache[isFirst][i]

        return max(dfs(0, True), dfs(1, False))