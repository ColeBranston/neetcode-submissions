import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stor = set([":", "'", ".","!", "?", ",", " "])
        tempword = ""

        for char in s:
            if char not in stor:
                tempword += char.upper()

        s = tempword
        
        for i in range(len(s) // 2):
            if i == 0 and s[i] != s[-1]:
                return False

            else:
                if s[i] != s[-i-1]:
                    return False

        return True

        