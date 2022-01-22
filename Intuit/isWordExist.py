def isWordExist(self, board, word):
		#Code here
		def dfs(i,j,strin):           
            
            if i>=len(board) or i<0:
                return False
            if j>=len(board[0]) or j<0:
                return False
            
            if board[i][j] == strin[0]:
                if len(strin) == 1:
                    return True
                kk = board[i][j]
                board[i][j]='#'
                cur1 = dfs(i+1,j,strin[1:])
                cur2 = dfs(i,j+1,strin[1:])
                cur3 = dfs(i-1,j,strin[1:])
                cur4 = dfs(i,j-1,strin[1:])
                res = (cur1 or cur2 or cur3 or cur4)
                board[i][j]=kk
                if res:
                    return True
                return False
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                if board[row][col] == word[0]:
                    cur = dfs(row,col,word)
                    if cur == True:
                        return True
        return False
