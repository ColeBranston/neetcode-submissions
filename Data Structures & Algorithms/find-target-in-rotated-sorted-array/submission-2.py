class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to find the pivot point, then binary search the two related

        l,r = 0,len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid

        pivot = l

        def binarySearch(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    return mid
            return -1

        res = binarySearch(0,pivot-1)
        if res != -1:
            return res

        return binarySearch(pivot, len(nums)-1)