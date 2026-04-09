class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                curr_area = min(heights[i],heights[j] ) * (j-i)
                if(curr_area > max_area):
                    max_area = curr_area
        return max_area

        