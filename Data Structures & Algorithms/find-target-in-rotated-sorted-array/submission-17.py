class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search for the pivot point, then binary search each halve

        def bSearch(array):
            l,r = 0, len(array)-1

            while l <= r:
                n = (l+r) // 2

                if array[n] < target:
                    l = n + 1
                elif array[n] > target:
                    r = n - 1
                else:
                    return n

            return -1

        l,r = 0, len(nums)-1

        while l < r:
            n = (l+r) // 2

            if nums[n] > nums[r]:
                l = n + 1

            else:
                r = n

        pivot = r

        first = bSearch(nums[:pivot]) 
        
        if first != -1:
            return first

        second = bSearch(nums[pivot:])

        return second + pivot if second != -1 else -1

        

        
        

