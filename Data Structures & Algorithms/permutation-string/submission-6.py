class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        Time: O(n * m²)
        Space: O(m)
        '''
        # l = 0
        # size = len(s1)

        # flag = False
        # for r in range(len(s2)):
        #     copy = list(s1)
        #     while r-l+1 > size:
        #         l+=1

        #     window = s2[l:r+1]
        #     for i in range(len(window)):
        #         if window[i] in copy:
        #             copy.remove(window[i])

        #         if not copy:
        #             flag = True
                
        # return True if flag else False

        '''
            O(n*m) create counter dictionaries for the first string and sliding window and compare them
            O(m)
        '''

        s1_counter = {}
        for char in s1:
            s1_counter[char] = s1_counter.get(char, 0) + 1

        s2_counter = {}

        l = 0
        size = len(s1)

        for r in range(len(s2)):
            while r-l+1 > size:
                l+=1

            for char in s2[l:r+1]:
                s2_counter[char] = s2_counter.get(char, 0)+1

            if s2_counter == s1_counter:
                print(s1_counter,s2_counter)
                return True

            s2_counter.clear()

        return False
