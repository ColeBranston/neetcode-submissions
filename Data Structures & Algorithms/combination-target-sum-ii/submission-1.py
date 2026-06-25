class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        check = set()

        def combination(i, curr, total):
            nonlocal output
            if total == target and tuple(curr) not in check:
                check.add(tuple(curr))
                return output.append(curr.copy())

            for j in range(i, len(candidates)):
                if total+candidates[j] > target: return
                if j > i and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[j])
                combination(j+1, curr, total+candidates[j])
                curr.pop()

        combination(0,[],0)
        return output