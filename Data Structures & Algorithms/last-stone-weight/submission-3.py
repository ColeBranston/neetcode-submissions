class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-stone for stone in stones]
        heapq.heapify(weights)

        while len(weights) != 1:
            stone_one = heapq.heappop(weights)
            stone_two = heapq.heappop(weights)

            heapq.heappush(weights, -abs(stone_one - stone_two))
        
        return -weights[0] if weights else 0
