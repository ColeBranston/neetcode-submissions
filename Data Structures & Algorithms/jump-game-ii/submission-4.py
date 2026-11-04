class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)-1
        cache = {}

        def dfs(i):
            nonlocal cache
            if i >= length:
                return 0
                
            if i in cache:
                return cache[i]

            minn = float('inf')
            for j in range(i+1, nums[i]+i+1):
                minn = min(minn, dfs(j))

            cache[i] = minn + 1
            return cache[i]

        return dfs(0)