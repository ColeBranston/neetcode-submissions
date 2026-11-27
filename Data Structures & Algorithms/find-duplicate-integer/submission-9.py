class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        slow, fast = 0, nums[0]
        while True:
            if nums[slow] == nums[fast]:
                return nums[slow]

            slow = nums[slow]
            fast = nums[nums[fast]]

        