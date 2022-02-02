def kthLargestNumber(self, nums: List[str], k: int) -> str:
        h = []
        for i in nums:
            heappush(h,int(i))
            if len(h)>k:
                heappop(h)
        res = heappop(h)
        return str(res)
