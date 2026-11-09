class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for string in strs:
            alphabet = [0] * 26

            for char in string: 
                index = ord(char) - ord('a')
                alphabet[index] += 1

            mapp[tuple(alphabet)].append(string)

        return [group for group in mapp.values()]