class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for string in strs:
            res.append(f'{len(string)}#{string}')

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)

        res = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])
            i += len(s[i:j]) + 1

            temp = ""
            for j in range(length):
                temp += s[i+j]
                
            i += length

            res.append(temp)

        return res

