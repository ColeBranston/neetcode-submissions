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
            print(l,n,r)

            if nums[n] > nums[r]:
                l = n + 1

            else:
                r = n

        pivot = r

        print(pivot, nums[:pivot], nums[pivot:])

        first = bSearch(nums[:pivot]) 
        second = bSearch(nums[pivot:])

        if second > first:
            return second + pivot
        else:
            return first

        

        
        

