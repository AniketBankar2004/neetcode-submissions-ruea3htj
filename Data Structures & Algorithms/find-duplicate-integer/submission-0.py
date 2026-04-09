class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_set = set()

        for num in nums:
            if num not in count_set:
                count_set.add(num)
            else:
                return num
      
        