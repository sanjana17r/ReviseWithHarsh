def calculateSpan(self,a,n):
        #code here
        stack = []
        res = [1]
        stack.append(0)
        for i in range(1,n):
            
            if not stack or a[i]<a[stack[-1]]:
                res.append(1)
                stack.append(i)
            else:
                while stack and a[stack[-1]]<=a[i]:
                    stack.pop()
                if not stack:
                    res.append(i+1)
                else:
                    res.append(i-stack[-1])
                stack.append(i)
        return res
