class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxx = 0
        l,r = 0,1

        if len(s) == 1:
            return 1

        if not s:
            return maxx

        stor = set(s[l])

        while r < len(s): # basically continue the window with r ensuring it doesn't go index out of range
            while s[r] in stor: # checking if the newest character isn't in the window
                stor.remove(s[l]) # if its a duplicate; removing the back of the window until its not (shifting), to maintain the longest window possible
                l+=1

            stor.add(s[r])
            maxx = max(maxx, r-l+1) # maxx is the size of the window (r-l+1) if its greater than the current maxx
            r+=1 # continue the edge of the window



        return maxx