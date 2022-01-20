def AllParenthesis(self,n):
        #code here
        if n==1:
            return ["()"]
        arr = []
        
        def backtracking(st,open,close):
            if len(st) == 2*n:
                arr.append(st)
                return
            if open<n:
                backtracking(st+"(",open+1,close)
            if close<open:
                backtracking(st+")",open,close+1)
        backtracking("",0,0)
        return arr
