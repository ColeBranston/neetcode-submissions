import math

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        similar to the other back tracking problems you just call the function with a choice
        and then backstep that choice, so in this instance, similar to previous you run a for loop
        through nums on each call and track already used numbers via a boolean array
        '''

        output = []
        picked = [False] * len(nums)
        
        def dfs(perm, nums, picked):
            nonlocal output
            if len(perm) == len(nums):
                output.append(perm.copy())

            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    perm.append(nums[i])
                    dfs(perm, nums, picked)
                    picked[i] = False
                    perm.pop()

        dfs([], nums, picked)
        return output
            
