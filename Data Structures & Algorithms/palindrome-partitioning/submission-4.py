class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(p):
            return p == p[::-1]

        def backtrack(pieces, i):
            # pieces[-1] is the "open" piece still being built
            if i == len(s):
                if isPali(pieces[-1]):          # close the final piece
                    res.append(pieces)
                return

            # Choice 1: extend the open piece (can't check it yet)
            backtrack(pieces[:-1] + [pieces[-1] + s[i]], i + 1)

            # Choice 2: close the open piece, start a new one
            if isPali(pieces[-1]):
                backtrack(pieces + [s[i]], i + 1)

        backtrack([s[0]], 1)
        return res