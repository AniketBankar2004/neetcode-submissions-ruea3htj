from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i,j])
        
        

        while(queue):
            x,y = queue.popleft()

            for r,c in ([1,0],[0,1],[-1,0],[0,-1]):
                a = x+r
                b = y+c

                if(a>=0 and b>=0 and a<m and b<n and grid[a][b]!=-1 
                and grid[a][b]!=0 and grid[a][b]>grid[x][y]+1):
                    queue.append([a,b])
                    grid[a][b] = 1 + grid[x][y]
                    
            


        