class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force, double itteraton -> Time: O(n^2), Space: O(n)

        res = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             res[i] *= nums[j]

        # return res

        # two pass, prefix-suffix solution -> Time: O(n), Space: O(n)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

