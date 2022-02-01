def findMaximumNum(self,s,k):
        
        def swap(i,j,s):
            s = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
            return s
        global maximum
        maximum = s
        def findMax(s,k):
            
            global maximum
            # print('cur max',maximum)
            if int(s)>int(maximum):
                maximum = s
            if k == 0:
                return
            for i in range(len(s)-1):
                for j in range(i+1,len(s)):
                    if s[j]<=s[i]:
                        continue
                    cur = s
                    s = swap(i,j,s)
                    # print('cur s',s)
                    if int(s)>int(maximum):
                        maximum = s
                    findMax(s,k-1)
                    s = cur
