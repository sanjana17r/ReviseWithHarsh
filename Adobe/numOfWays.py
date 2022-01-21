def numOfWays(self, n, x):
        # code here
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        maxLimit = int(n**(1/x))

        for i in range(2, maxLimit+1):
            curr = i**x
            for j in range(n,curr-1,-1):
                dp[j] += dp[j-curr]
        mm = 1000000007
        return dp[n]%mm
