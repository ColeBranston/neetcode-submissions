class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def recurse(index, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            for j in range(index, len(nums)):
                if total + nums[j] > target:
                    return
                
                curr.append(nums[j])
                recurse(j, curr, total+nums[j])
                curr.pop()

        recurse(0,[],0)
        return res