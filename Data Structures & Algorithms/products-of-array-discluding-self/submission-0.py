class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        stor = []

        for i in range(len(nums)):
            prod = 1
            tempArray = nums[:i] + nums[i+1:]

            for j in tempArray:
                prod *= j

            stor.append(prod)

        return stor
