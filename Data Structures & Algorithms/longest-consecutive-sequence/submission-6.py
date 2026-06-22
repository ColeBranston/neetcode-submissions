class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stor = []

        if not nums:
            return 0

        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                tempNum = num
                boolean = True
                counter = 1

                while boolean:
                    if tempNum + 1 in nums:
                        print("Current:", tempNum, "Next: ", tempNum + 1)
                        counter += 1
                        tempNum += 1

                    else:
                        boolean = False
                        stor.append(counter)

        return max(stor)
