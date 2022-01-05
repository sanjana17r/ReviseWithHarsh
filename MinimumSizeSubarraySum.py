def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        q = deque()
        n = len(nums)
        sum = 0
        flag = 0
        for i in range(n):
            sum+=nums[i]
            q.append(nums[i])
            while sum>=target:
                flag = 1
                minLen = min(minLen,len(q))
                sum-=(q.popleft())
        if flag == 0:
            return 0
        return minLen
