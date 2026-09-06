class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        manage the indexes of the largest numbers in each window of the nums array.
        you manage the que by unqueing the latest index if the number at that index is less 
        than the new element being added to the window. for each cycle you check 
        if the left pointer of the window is greater than the index
        stored at the end of the que, and cycle it with pop left if it is to ensure that the 
        number that is later cycled into the output array coresponds with the window at hand.

        '''

        output = []
        q = deque()

        l,r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k: # or r >= k-1
                output.append(nums[q[0]])
                l+=1

            r+=1

        return output

