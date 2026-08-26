class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            n = (l+r)//2
            if nums[n] < nums[r]:
                r = n
            else:            
                l = n + 1
        
        return nums[r] # can be either l or r, since they never actually cross since its lower bounded