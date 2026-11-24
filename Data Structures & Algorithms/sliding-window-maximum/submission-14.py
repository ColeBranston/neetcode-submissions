class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # you need to slide through keeping tracking of the largest number at each window point

        l = 0
        r = 0

        res = []

        q = deque()

        while r < len(nums):
            if r-l+1 > k:
                l += 1

            # print(q)
            while q and (nums[r] > q[-1][0]):
                # print("Getting rid of: ", q[-1])
                q.pop()

            q.append((nums[r], r))

            while q and not l <= q[0][1] <= r:
                q.popleft()

            res.append(q[0])
            
            r += 1

        return [num for num,index in res[k-1:]]

            


            