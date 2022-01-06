def maxSubArray(self, nums: List[int]) -> int:
        req = -sys.maxsize+1
        cur = 0
        for i in range(len(nums)):
            cur+=nums[i]
            
            if cur<nums[i]:
                cur = nums[i]
            req = max(req,cur)
            
        return req
