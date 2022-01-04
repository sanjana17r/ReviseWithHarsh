def findTwoElement( self,arr, n): 
        # code here
        res = []
        sum1 = n*(n+1)//2
        sq1 = (n*(n+1)*(2*n+1))//6
        sum2 = 0
        sq2 = 0
        for i in arr:
            sum2+=i
            sq2 += (i**2)
        k = sum1-sum2
        y = (sq1-sq2)//k
        res.append((y-k)//2)
        res.append((k+y)//2)
        return res
