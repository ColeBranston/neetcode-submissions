class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}

        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1

        res = list(mapp.items())

        res.sort(key=lambda x: x[1])

        res = [num[0] for num in res[len(res)-k:]]

        return res