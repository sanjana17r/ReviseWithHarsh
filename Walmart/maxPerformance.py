def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        res = sSum = 0
        # min heap contains speed, keep adding elements until it crosses k
        # if corsses k then subtract the least element from it
        # we are multiplying the current efficiency each time, as current is going to be minimum out of all
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h,s)
            sSum+=s
            if len(h)>k:
                k1 = heapq.heappop(h)
                sSum-=k1
            res = max(res,sSum*e)
        return res % (10**9 + 7)
