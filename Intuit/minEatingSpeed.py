import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort()
        lo = 1
        hi = max(piles)
        if h == len(piles):
            return hi
        ans = hi
        def isPoss(mid):
            count = 0
            arr = piles[:]
            l,r = 0,0
            for i in range(r,len(arr)):
                k = math.ceil(arr[i]/mid)
                count+=k
            r = l
            return count<=h
        while lo<=hi:
            mid = (lo+hi)//2
            if isPoss(mid):
                ans = min(mid,ans)
                hi = mid-1
            else:
                lo=mid+1
        return ans
