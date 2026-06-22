class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            typically the minn variable can be found in a sorted array by just taking the first element. Because its spiral we will have to do something different.

Binary Search:

	Your typical binary search question contains the following:
		- a left and right pointer starting at the first and last index of the array
		- a while loop with a n pointer calculated as the middle between the two left+right pointers
		ie. (l+r)//2
		- if the target element is less than the middle most element with pointer n, you shift the right
		pointer to the nth - 1 position and recalculate n when you next loop around. If the target element 		is greater than the nth element then the l pointer is moved to the nth + 1 position and once again, 		the nth index is recalculated with the following loop around. 

Context of this problem:
	This problem essentially has an ascendingly sorted array for binary search, but that's been rotated where
	the last n elements have been moved to the start of the array. The goal of the problem is through using 	binary search to find the minimum element ie. min number

Thinking:
	- in a way there will always be at a maximum of two sub arrays: the rotated portion and the original 	portion, so If I could figure out where those sub arrays were I could find the first element in that second	sub array.
	
	Potential Solution: Use binary search to check where the right pointer value < left pointer value, then 	return the right pointer value. Otherwise if there are no instances of r < l, then return the first 	element because in that case the array hasn't been rotated at all.
        '''

        l,r = 0, len(nums)-1

        if len(nums) == 1:
            return nums[0]

        while l<r:
            n = (r+l)//2
            print("L: ", l,"R: ",r, "N: ", n, "nums[n]: ", nums[n])

            if nums[l] > nums[r]:
                if nums[r-1] < nums[r]:
                    r-=1
                else:
                    return nums[r]

            elif nums[l] < nums[r]:
                r = n

        return nums[r]
            

        

        
