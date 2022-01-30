def height(self, N):
        # code here
        l = 0
        r = N
        ans = 0
        while l<=r:
            i = l+ (r-l)//2
            if i*(i+1) <= 2*N:
                ans = i
                l = i+1
            else:
                r = i-1
        return ans
