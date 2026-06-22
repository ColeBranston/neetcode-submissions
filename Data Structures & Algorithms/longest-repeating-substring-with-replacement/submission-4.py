class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freq = {}
        maxFreq = 0
        maxSize = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1 # tracks the frequency of the char in the window
            maxFreq = max(maxFreq, freq[s[r]]) # reassigns the max frequency by checking the current frequency of the char in the window

            while (r-l+1) - maxFreq > k: # shrinks the window if the number of chars other than the most common goes above the k number of transformations (maintains the window)
                freq[s[l]] -= 1
                l+=1

            maxSize = max(maxSize, r-l+1) # re assigns the max continues substring by checking the window size representing the max number of possible continous characters
            r+=1 # continues the window

        return maxSize