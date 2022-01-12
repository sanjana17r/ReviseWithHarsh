def subsetSum(self, arr, Sum, n):
       dp = [[-1 for _ in range(Sum+1)] for _ in range(n+1)]

       for j in range(Sum+1):
           dp[0][j] = False
       for i in range(n+1):
           dp[i][0] = True
   
       for i in range(1, n+1):
           for j in range(1, Sum+1):
               if arr[i-1] <= j:
                   dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
               else:
                   dp[i][j] = dp[i-1][j]
       
       size = (Sum//2) + 1
       subsetSum_s1 = []
       for k in range(size):
           if dp[n][k] == True:
               subsetSum_s1.append(k)


       return subsetSum_s1
   
   
   
    def minDifference(self, arr, n):
           total_Sum = 0
           for i in range(n):
               total_Sum += arr[i]
           
           minDiff = float('inf')
           subsetSum_s1 = self.subsetSum(arr, total_Sum, n)
           size_s1 = len(subsetSum_s1)
           for i in range(size_s1):
               curr_minDiff = total_Sum - 2*subsetSum_s1[i]
               minDiff = min(minDiff, curr_minDiff)
           
           return minDiff
