def minDifference(self, arr, n):
		# code here
		arr.sort()
		l,r=0,n-1
		dp1 = [0]*n
		dp1[0] = arr[0]
		dp2 = [0]*n
		dp2[-1] = arr[-1]
		for i in range(1,n):
		    dp1[i]+=(dp1[i-1]+arr[i])
		for i in range(n-2,-1,-1):
		    dp2[i]+=(dp2[i+1]+arr[i])
		diff = float('inf')
# 		dp1 = dp1[::-1]
		for i in range(n-1,0,-1):
		    diff = min(diff,abs(dp2[i]-dp1[i-1]))
		return diff
