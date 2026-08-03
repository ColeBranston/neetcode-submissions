class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        freqArray = [(u,v) for u,v in freq.items()]

        freqArray.sort(key=lambda x: x[1])

        res = freqArray[len(freqArray)-k:]

        return [num for num,frequency in res]