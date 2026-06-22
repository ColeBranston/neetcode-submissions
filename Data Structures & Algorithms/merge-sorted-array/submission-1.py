class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        else:
            for i in range(n):
                nums1.pop()

            for num in nums2:
                nums1.append(num)

            nums1.sort()


        