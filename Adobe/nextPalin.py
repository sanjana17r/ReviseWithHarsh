def nextPalin(self,N):
        #code here
        l = math.floor(len(N)/2)
        
        string = N[:l]
        string = list(string)
        # print("length is ",l,'string is ',string)
        flag = 0
        if len(N)%2 == 1:
            flag = 1
            
        stack = []
        for i in range(l-1,-1,-1):
            if not stack:
                stack.append((string[i],i))
            elif stack[-1][0]<string[i]:
                stack.append((string[i],i))
            else:
                
                while stack and stack[-1][0]>string[i]:
                    cur,ind = stack.pop()
                # print("index is ",ind,'curr is ',i)
                try:
                    string[i],string[ind] = string[ind],string[i]
                except:
                    continue
                k = string[i+1:ind+1]
                k.sort()
                # print("string is ",string,'k is ',k)
                
                string[i+1:ind+1] = k[:]
                string = ''.join(string)
                if flag == 1:
                    string = string+N[l]+string[::-1]
                else:
                    string = string+string[::-1]
                return string
        return '-1'
