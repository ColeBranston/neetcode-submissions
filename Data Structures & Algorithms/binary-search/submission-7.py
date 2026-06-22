class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            n = (l+r) // 2
            if target > nums[n]:
                l = n + 1
            elif target < nums[n]:
                r = n - 1
            elif nums[n] == target:
                return n

        return -1