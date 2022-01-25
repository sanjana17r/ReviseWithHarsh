def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis = set()
        count = 0
        def dfs(cur):
            for j in range(len(isConnected)):
                if (isConnected[cur][j]==1) and (j not in vis):
                    vis.add(j)
                    dfs(j) #check if any city connected to this city
            
        
        for i in range(len(isConnected)):
            if i not in vis:
                count+=1
                vis.add(i)
                dfs(i)#check if any city connected to this city
        return count
