class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        for num in nums:
            if(num in map):
                map[num]+=1
            else:
                map[num]=1
        
        for count in map.values():
            if count > 1:
                return True
        
        return False



            


            