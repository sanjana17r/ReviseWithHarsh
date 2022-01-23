def isPossible(self,weights,mid,days):
        curSum = 0
        day = 1
        for i in weights:
            curSum+=i
            if curSum>mid:
                curSum =i
                day+=1
        return day<=days
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        ans = float('inf')
        if len(weights) == days:
            return lo
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if self.isPossible(weights,mid,days):
                ans = min(ans,mid)
                hi=mid-1
            else:
                lo=mid+1
        return ans
