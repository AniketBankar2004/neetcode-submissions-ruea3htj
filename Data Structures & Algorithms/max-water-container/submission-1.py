class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        l = 0
        r =len(heights)-1
        
        while (l<r):
            area = (r-l) * min(heights[l], heights[r])
            max_area = max(area,max_area)
            if heights[l] >= heights[r]:
                r = r -1
            else:
                l = l+1
            
        return max_area
        