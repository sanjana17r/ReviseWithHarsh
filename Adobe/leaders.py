def leaders(self, A, N):
        #Code here
        stack = []
        res = []
        A.reverse()
        for i in range(len(A)):
            if i == 0:
                res.append(A[0])
                stack.append(A[0])
            else:
                if stack[-1]>A[i]:
                    continue
                else:
                    res.append(A[i])
                    stack.append(A[i])
        return res[::-1]
