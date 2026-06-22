import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split(" ")).upper()
        stor = set([":", "'", ".","!", "?", ","])
        tempword = ""

        for char in s:
            if char not in stor:
                tempword += char 

        s = tempword
        
        for i in range(math.floor(len(s) / 2)):
            if i == 0 and s[i] != s[-1]:
                print(s, "i: ", i)
                return False

            else:
                if s[i] != s[-i-1]:
                    print(s, "i: ", i)
                    return False

        print(s)
        return True

        