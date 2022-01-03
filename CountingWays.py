def CountWays(self, s):
	    if s[0]=="0" or s[-1] == '0' or '00' in s:
	        return 0
	    if len(s) == 0:
            return 0

        dp = [0 for x in range(len(s) + 1)] 
        dp[0] = 1 
        dp[1] = 1 
        if s[0] == "0":
            return 0

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        return dp[len(s)]
