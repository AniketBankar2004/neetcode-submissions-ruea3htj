import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        res = [] 

        for point in points:
            heapq.heappush(heap,[point[0]**2 + point[1]**2,point])
        

        for i in range(k):
            point  = heapq.heappop(heap)
            res.append(point[1])
        
        return res

        


        