class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            n = (l+r) // 2

            if nums[r] < nums[n]:
                l = n + 1

            else:
                r = n - 1

            res = min(res, nums[n])

        return res