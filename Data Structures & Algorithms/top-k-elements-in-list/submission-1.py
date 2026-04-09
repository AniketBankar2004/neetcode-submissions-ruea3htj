import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] =1
            else:
                counter[num] +=1

        
        for num,count in counter.items():
            heapq.heappush(heap,(-count,num))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        