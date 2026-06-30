class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-stone for stone in stones]
        heapq.heapify(weights)

        while len(weights) != 1:
            print(weights)
            if len(weights) == 1: break
            stone_one = heapq.heappop(weights)
            stone_two = heapq.heappop(weights)

            diff = -abs(stone_one - stone_two)

            heapq.heappush(weights, diff)
        
        return -weights[0] if weights else 0
