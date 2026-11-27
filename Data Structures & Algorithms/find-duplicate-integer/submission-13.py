class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        In no way is this a linked list question
        '''

        # stor = set()
        # for nums in nums:
        #     if nums in stor:
        #         return nums
        #     stor.add(nums)
        # return 0
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

