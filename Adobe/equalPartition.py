def equalPartition(self, N, nums):
        # code here
        sums = sum(nums)
        if sums%2 == 1:
            return False
        dp = {0}
        target = sums//2
        for i in range(len(nums)):
            nextDp = set()
            for t in dp:
                if t+nums[i] == target or nums[i] == target:
                    return True
                nextDp.add(t+nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False  
