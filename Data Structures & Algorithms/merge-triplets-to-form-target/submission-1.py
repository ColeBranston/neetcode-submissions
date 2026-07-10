class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        indicator = 0
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            if t[0] == target[0]:
                good.add(0)
            if t[1] == target[1]:
                good.add(1)
            if t[2] == target[2]:
                good.add(2)

        return len(good) == 3