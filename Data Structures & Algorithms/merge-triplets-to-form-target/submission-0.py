class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag = [False] * 3

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            if t[0] == target[0]:
                flag[0] = True

            if t[1] == target[1]:
                flag[1] = True

            if t[2] == target[2]:
                flag[2] = True

        return flag[0] and flag[1] and flag[2]