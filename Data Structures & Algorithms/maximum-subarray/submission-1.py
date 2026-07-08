class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        temp = 0
        for num in nums:
            if temp < 0:
                temp = 0

            temp += num
            maxx = max(maxx, temp)

        return maxx