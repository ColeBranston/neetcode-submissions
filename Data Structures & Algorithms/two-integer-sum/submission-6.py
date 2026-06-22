class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stor = {}
        temp = []

        if len(nums) == 2:
            return [0,1]

        for num in nums:
            if num not in stor:
                stor[target - num] = num

            elif num in stor and num*2 == target:
                ind1 = nums.index(num)
                nums.remove(nums[ind1])
                return [ind1, nums.index(num)+1]

            else:
                return [nums.index(stor[num]), nums.index(num)]

        print(stor)
        return []