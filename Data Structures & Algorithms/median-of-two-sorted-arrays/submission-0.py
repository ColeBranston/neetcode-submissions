class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)

        nums1.sort()

        print(nums1)

        if len(nums1) % 2 == 0:
            floorMid = len(nums1)//2
            print(nums1[floorMid], nums1[floorMid-1])
            return (nums1[floorMid] + nums1[floorMid-1])/2

        return nums1[len(nums1)//2]
