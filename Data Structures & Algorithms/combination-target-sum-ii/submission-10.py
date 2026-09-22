class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        seen = set() # doesns't have to be a set, can be an array since the curr_element == prev_element check stops duplicates
        candidates.sort()

        def backtrack(array, total, index):
            if total == target:
                seen.add(tuple(array.copy()))
                return
                
            for i in range(index, len(candidates)):
                if total + candidates[i] > target:
                    break

                if i > index and candidates[i] == candidates[i-1]:
                    continue

                array.append(candidates[i])
                backtrack(array, total + candidates[i], i+1)
                array.pop()

        backtrack([], 0, 0)
        return [list(tup) for tup in seen]