class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        left = 0
        while l <= r:
            n = (l+r)//2
            print(l,r, n)
            if nums[n] > nums[r]:
                l = n+1
                left = l

            elif nums[n] < nums[r]:
                r = n

            else:
                return nums[n]
        
        return nums[left+1]