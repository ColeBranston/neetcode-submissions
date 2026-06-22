class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        size = len(s1)

        flag = False
        for r in range(len(s2)):
            copy = list(s1)
            while r-l+1 > size:
                l+=1

            window = s2[l:r+1]
            for i in range(len(window)):
                if window[i] in copy:
                    copy.remove(window[i])

                if not copy:
                    flag = True
                
        return True if flag else False
