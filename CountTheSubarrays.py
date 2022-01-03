def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        l = 0
        r = 0
        p = 1
        count = 0
        while r<n:
            p*=a[r]
            while l<r and p>=k:
                # l+=1
                p = p//a[l]
                l+=1
            if p<k:
                count+=(r-l+1)
            r+=1
        return count
