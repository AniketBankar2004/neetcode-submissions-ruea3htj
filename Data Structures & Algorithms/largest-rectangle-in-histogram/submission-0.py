class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stack = []
        for idx,height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                j,h = stack.pop()
                w = idx - j
                a = w * h
                start = j
                max_area = max(a,max_area)
            stack.append([start,height])
        
        while stack :
            j,h = stack.pop()
            w = n - j
            area = h * w
            max_area = max(area,max_area)
        return max_area


        