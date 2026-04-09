class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        mid = (l+r) // 2

        def can_eat(speed):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/speed)
            
            if hrs <= h:
                return True
            else :
                return False

        while l<=r:
            mid = (l+r)//2
            if can_eat(mid):
                ans = mid
                r = mid -1
            else:
                l = mid + 1
        return ans
                


        