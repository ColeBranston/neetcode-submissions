class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        wQ = deque()
        l,r = 0,0
        res = []

        while r < len(nums):
            while wQ and nums[wQ[-1]] < nums[r]:
                wQ.pop()

            wQ.append(r)

            if l > wQ[0]:
                wQ.popleft()

            if r-l+1 >= k:
                res.append(nums[wQ[0]])
                l+=1

            r+=1

        return res
