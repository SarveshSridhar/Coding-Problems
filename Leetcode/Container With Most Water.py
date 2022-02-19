class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        start = 0
        end = len(height)-1
        for _ in range(len(height)):
            if height[start]<height[end]:
                res = (end-start)*(height[start])
                start+=1
            elif height[start]>=height[end]:
                res = (end-start)*height[end]
                end-=1
            water = max(water,res)
        return water
