class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) >= len(nums2):
            larger = nums1
            smaller = nums2

        else:
            larger = nums2
            smaller = nums1

        check = set(smaller)
        res = set()
        for num in larger:
            if num in check:
                res.add(num)

        return list(res)