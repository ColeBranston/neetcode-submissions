class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums)-1
        while k:
            val = nums.pop()
            nums.insert(0, val)
            k-=1