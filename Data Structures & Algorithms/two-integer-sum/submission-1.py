class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        index={}
        for i,j in enumerate(arr):
            diff=target -  j
            if diff in index:
                return [index[diff],i]
            else:
                index[j]=i
        