class Solution:
    def encode(self, strs: List[str]) -> str:
        res = f'{len(strs)}α'

        res += "δ".join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        length, strings = s.split("α")

        stringArray = strings.split("δ")

        return stringArray if int(length) >= 1 else []