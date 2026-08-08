class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.upper() for char in s]
        forbidden = set([' ', '?', ',', "'", ".", ":", "!"])
        sArray = [(char if char not in forbidden else '') for char in s]
        s = ''.join(sArray)

        start,end = 0, len(s)-1
        print(s)

        if len(s) == 1:
            return True

        while start < end:
            if s[start] != s[end]:
                print("start: ", s[start])
                print("end: ", s[end])
                return False

            start +=1
            end -=1

        return True