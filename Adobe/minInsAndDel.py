def minInsAndDel(self, A, B, N, M):
       count = 0
       if(N == 0 and M == 0):
           return count
       for i in range(M):
           try:
               if(A[i] != B[i]):
                   A.pop(i)
                   count += 1
                   A.insert(i, B[i])
                   count += 1
           except:
                break
       count += abs(N-M)
       return count
