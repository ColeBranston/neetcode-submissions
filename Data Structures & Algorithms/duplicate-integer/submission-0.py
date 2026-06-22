class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stor = set()
        for n in nums:
            stor.add(n)
        
        return not (len(stor) == len(nums))

        
