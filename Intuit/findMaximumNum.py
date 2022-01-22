def findMaximumNum(self,s,k):
        #code here
        def swap(st,i,j):
            left = st[:i]
            ith = st[i]
            middle = st[i+1:j]
            jth = st[j]
            right = st[j+1:]
            return (left + jth + middle + ith + right)
        def recursion(s,k,maxn):
            if int(s) > maxn:
                maxn = int(s)
            if k==0:
                return maxn
            for i in range(len(s)-1):
                for j in range(i+1,len(s)):
                    if int(s[i]) < int(s[j]):
                        s = swap(s,i,j)
                        maxn = recursion(s,k-1,maxn)
                        s = swap(s,i,j)
            return maxn
        maxn = 0
        return recursion(s,k,maxn)
        return str(maxn)
