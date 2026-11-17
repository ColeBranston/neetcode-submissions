class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            rate = (l + r) // 2
            hours = sum(math.ceil(p / rate) for p in piles)

            if hours <= h:      # fast enough → record it, try slower
                res = rate
                r = rate - 1
            else:               # too slow → go faster
                l = rate + 1

        return res