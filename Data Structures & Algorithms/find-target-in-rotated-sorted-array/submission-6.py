class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            
            while l <= r:
                n = (l+r)//2
                if target < nums[n]:
                    r = n-1
                elif target > nums[n]:
                    l = n+1
                else:
                    return n
            
            return -1
            
        l,r = 0, len(nums)-1

        while l < r:
            n = (l+r) // 2

            if nums[n] > nums[r]:
                l = n+1
            else:
                r = n

        pivot = l # could be l or r doesn't matter
        
        res = binarySearch(0, pivot-1)
        
        if res != -1:
            return res

        return binarySearch(pivot, len(nums)-1)
        



        

            