class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        '''
        Kadanes algo works here because theoretically the currMin and currMax are greatest in terms
        of magnitude so simply keeping track of them each time allows you to always have the greatest subarray size
        no matter if a -ve number makes the max the min, since in that instance the currMin would become the max
        '''
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res