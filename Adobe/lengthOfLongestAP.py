def lengthOfLongestAP(self, nums, n):
        # code here
        # n = len(nums)
        dp = [{} for i in range(n)]#initialize with dictionaries
        ans = 0
        for i in range(n):
            dp[i][0]=1
            for j in range(i):
                dif = nums[i]-nums[j]
                if dif not in dp[j]:
                    dp[i][dif]=2
                else:
                    dp[i][dif] = dp[j][dif]+1
            ans = max(a
