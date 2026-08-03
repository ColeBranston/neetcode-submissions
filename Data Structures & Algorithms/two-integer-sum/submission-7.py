class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stor = {}

        if not nums: return [-1,-1]

        for i in range(len(nums)):
            if nums[i] not in stor:
                stor[target-nums[i]] = i

            else:
                return [stor[nums[i]],i]

        return [-1, -1]