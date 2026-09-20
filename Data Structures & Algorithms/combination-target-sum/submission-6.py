class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()

        def backtrack(curr, total, index):
            nonlocal seen

            if total == target:
                seen.add(tuple(curr.copy()))
                return

            for i in range(index, len(nums)):
                if total + nums[i] <= target:
                    curr.append(nums[i])
                    backtrack(curr, total+nums[i], i)
                    curr.pop()

        backtrack([], 0, 0)
        return [list(tup) for tup in seen]
