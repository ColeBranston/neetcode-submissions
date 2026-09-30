class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, f in freq.items():
            heapq.heappush(heap, (f,num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for f, num in heap]

        