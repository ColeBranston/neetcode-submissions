class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Kadane's algo is basically the idea that once a subarray becomes negative it decreases
        any future sub array, so it would make sense just to start a new sub array from that point
        onwards. By comparing the max subarray size to the current subarray each time, even if the
        subarray is before or after the global max will always track it
        '''

        maxx = nums[0] # max subarray is at min the first element (first to take into consideration a list of size of one)
        temp = 0

        for num in nums:
            if temp < 0:
                temp = 0 

            temp += num
            maxx = max(maxx, temp)

        return maxx
        