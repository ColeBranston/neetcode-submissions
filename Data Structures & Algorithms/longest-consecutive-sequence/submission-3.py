class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stor = []

        if not nums:
            return 0
            
        for num in nums:
            
            MaxCounter = 0
            tempNum = num   
            boolean = True
            counter = 1

            while boolean:
                if tempNum + 1 in nums:
                    print("Current:",tempNum, "Next: ", tempNum + 1)
                    counter += 1
                    tempNum += 1
                
                else:
                    boolean = False
                    stor.append(counter)
        
        return max(stor)