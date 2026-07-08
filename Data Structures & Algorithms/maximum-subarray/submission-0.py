class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float('-inf')

        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]

                maxx = max(maxx, temp)

        return maxx