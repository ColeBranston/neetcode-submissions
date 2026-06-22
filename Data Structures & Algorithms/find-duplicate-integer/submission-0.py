class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stor = set()

        for nums in nums:
            if nums in stor:
                return nums

            stor.add(nums)

        return 0