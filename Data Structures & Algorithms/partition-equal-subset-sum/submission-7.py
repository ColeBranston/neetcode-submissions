class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        desired = total // 2

        cache = defaultdict(dict)

        nums.sort()
        print(nums)
        def dfs(i, curr):
            if curr == desired:
                return True
            
            elif curr > desired or i >= len(nums):
                return False

            elif i in cache and curr in cache[i]:
                return cache[i][curr]
            
            res = dfs(i+1, curr + nums[i]) or dfs(i+1, curr)
            
            cache[i][curr] = res
            return res

        return dfs(0,0)