class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minn, maxx = 1, 1

        for num in nums:
            temp = num * maxx
            maxx = max(num * maxx, num * minn, num)
            minn = min(temp, num * minn, num)

            res = max(res, maxx)

        return res