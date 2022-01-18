def possibleWords(self,digits,N):
        #Your code here
        if len(digits) == 0:
            return []
        maping = [0,1,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        def backtrack(cur,index):
            if index == len(digits):
                res.append(cur)
                return
            k = int(digits[index])
            letters = maping[k]
            for j in letters:
                backtrack(cur+j,index+1)
        backtrack('',0)
        return res
