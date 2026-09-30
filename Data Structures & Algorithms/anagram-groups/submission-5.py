class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in range(len(strs)):
            freq = [0] * 26

            for char in strs[i]:
                freq[ord(char) - ord('a')] += 1

            res[tuple(freq)].append(strs[i])

        return [val for val in res.values()]
        
        