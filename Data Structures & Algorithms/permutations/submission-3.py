class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)

        def backtrack(curr, used):
            if len(curr) == size:
                res.append(curr.copy())
                return

            for num in nums:
                if num not in used:
                    curr.append(num)
                    used.add(num)
                    backtrack(curr, used)
                    curr.remove(num)
                    used.remove(num)
                
        backtrack([], set())
        return res