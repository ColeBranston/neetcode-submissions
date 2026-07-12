class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        '''
        although we want the largest number of partitions we also have to understand that
        any character in between the first character and its last reference must also be included
        in the current partition if its not the last character of its kind. Therefore, we want to 
        include the last index of every character in the string, and itterate through each character
        again saving a size of paritition var while checking and saving against the last index of 
        the current character and the greatest last index of the characters currently in the partition.
        If the current index is equal to the lastIndex (in this case "end") then you append the size
        to the res array and start a new partition by resetting the counter var to 0
        '''

        for i, v in enumerate(s):
            last[v] = i
        
        res = []
        size = end = 0
        for i, v in enumerate(s):
            size += 1

            end = max(end, last[v])

            if i == end:
                res.append(size)
                size = 0

        return res