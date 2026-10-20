class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        localMax = 0
        for num in nums:
            localMax += num

            res = max(res, localMax)

            if localMax <= 0:
                localMax = 0

        return res