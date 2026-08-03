class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        freqArray = [(u,v) for u,v in freq.items()]

        for i in range(k):
            maxx = max(freqArray, key=lambda x: x[1])
            res.append(maxx)
            freqArray.remove(maxx)

        return [num for num,frequency in res]