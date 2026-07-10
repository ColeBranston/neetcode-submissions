class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        indicator = 0
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t): # have to add either 1, 2, or 3 because you can have multiple matches of the same column until you get the others, so using an increasing counter could give you false positives 
                if v == target[i]:
                    good.add(i)

        return len(good) == 3