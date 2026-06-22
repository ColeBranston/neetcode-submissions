import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stor = set([":", "'", ".","!", "?", ",", " "])
        tempword = ""

        for char in s:
            if char not in stor:
                tempword += char.upper()

        s = tempword

        print(s)
        
        for i in range(math.floor(len(s) / 2)):
            if i == 0 and s[i] != s[-1]:
                return False

            else:
                if s[i] != s[-i-1]:
                    return False

        return True

        