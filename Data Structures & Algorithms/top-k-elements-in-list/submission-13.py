class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stor = {}

        for num in nums:
            if num not in stor:
                stor[num] = nums.count(num)
                print(stor.items())

        returnArray = []

        for i in range(k):

            maxCount = max(list(stor.values()))
            maxNum = list(stor.keys())[list(stor.values()).index(maxCount)]

            print("maxCount:", maxCount, "\nmaxNum:", maxNum)
            returnArray.append(maxNum)

            del stor[maxNum]

        return returnArray
