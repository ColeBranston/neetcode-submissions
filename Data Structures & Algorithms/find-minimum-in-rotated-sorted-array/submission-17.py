class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            n = (l+r)//2
            print(l,r,n)
            if nums[n] < nums[r]:
                r = n
                left = l
            else:            
                l = n + 1
        
        return nums[l]