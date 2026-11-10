class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = []
        s = s.lower()

        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz1234567890":
                clean.append(char)

        s = ''.join(clean)

        l,r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True