class Solution:
    def trap(self, height: List[int]) -> int:
        totalSum = 0

        for i in range(1, len(height) - 1):  # Skip edges
            left_max = max(height[:i])
            right_max = max(height[i:])

            totalSum += max(min(left_max, right_max) - height[i], 0)

        return totalSum
