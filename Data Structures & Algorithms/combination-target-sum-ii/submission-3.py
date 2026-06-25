class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def combination(i, curr, total):
            nonlocal output
            if total == target:
                output.append(curr.copy())
                return 

            for j in range(i, len(candidates)):
                if total+candidates[j] > target: return
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                combination(j+1, curr, total+candidates[j])
                curr.pop()

        combination(0,[],0)
        return output