class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'None'
        return 'and'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        splitt = s.split('and')
        return splitt