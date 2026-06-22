class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for i in range(len(height)):
            leftMax = max(height[:i+1])
            rightMax = max(height[i:])

            water += min(leftMax, rightMax) - height[i]

        return water