class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        if not nums:
            return -1

        if nums[0] == target:
            return 0

        while l < r:
            n = r-l // 2
            if target > nums[n]:
                l = n + 1
            elif target < nums[n]:
                r = n - 1
            elif nums[n] == target:
                return n

        return -1