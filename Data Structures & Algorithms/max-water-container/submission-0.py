class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area =0
        while l<r:
            width = r-l
            min_height = min(height[r],height[l])
            area = max(area, width*min_height)

            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return area