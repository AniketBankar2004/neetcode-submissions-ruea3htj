class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        l=0
        r = num_rows * num_cols -1

        while l<=r:
            mid = (l+r)//2
            row = mid // num_cols
            col = mid % num_cols
            mid_value = matrix[row][col]

            if target == mid_value:
                return True
            elif target > mid_value:
                l = mid +1
            elif target < mid_value:
                r = mid -1

        return False 

        
            

        


        

        


        