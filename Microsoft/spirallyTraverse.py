def spirallyTraverse(self,matrix, r, c): 
        # code here 
        res = []
        bottom = len(matrix)
        if bottom == 0:
            return res
        left = 0
        right = len(matrix[0])
        if right == 0:
            return res
        top = 0
        size = bottom*right
        count = 0
        while (right>left) and (bottom>top) and (count<size):
            for i in range(left,right):
                count+=1
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bottom):
                count+=1
                res.append(matrix[i][right-1])
            
            right-=1
            for i in range(right-1,left-1,-1):
                count+=1
                res.append(matrix[bottom-1][i])
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                count+=1
                res.append(matrix[i][left])
            left+=1
        return res[:size]
