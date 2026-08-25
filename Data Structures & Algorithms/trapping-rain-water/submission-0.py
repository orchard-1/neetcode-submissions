class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r= len(height)-1
        ans = 0
        lmax =height[l]
        rmax =height[r]

        while l < r:
            if lmax < rmax:
                ans+= lmax-height[l]
                l+=1
                lmax = max(lmax,height[l])
            else:
                ans+= rmax-height[r]
                r-=1
                rmax = max(rmax,height[r])
        return ans