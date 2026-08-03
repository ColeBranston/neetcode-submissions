class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in range(len(strs)):
            chars = [0] * 26

            for c in strs[i]:
                chars[ord(c)-ord('a')] += 1

            res[tuple(chars)].append(strs[i])

        return list(res.values())