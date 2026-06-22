class Solution:
    def trap(self, height: List[int]) -> int:
        # water = 0

        # for i in range(len(height)):
        #     left = max(height[:i+1])
        #     right = max(height[i:])

        #     water += min(left, right) - height[i]

        # return water

        water = 0
        
        l,r = 0, len(height)-1
        leftMax, rightMax = 0,0

        while l < r:
            if height[l] > height[r]:
                if height[r] > rightMax:
                    rightMax = height[r]

                else:
                    water += rightMax - height[r]

                r -= 1
            else:
                if height[l] > leftMax:
                    leftMax = height[l]

                else:
                    water += leftMax - height[l]

                l += 1
        
        return water
                
