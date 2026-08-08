class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.upper() for char in s]
        allowed = set([char for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQYZ0987654321'])
        sArray = [(char.upper() if char in allowed else '') for char in s]
        s = ''.join(sArray)

        start,end = 0, len(s)-1

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