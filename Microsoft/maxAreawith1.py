def findMaxArea(self, grid):
        #Code here
        m = 0
        def dfs(i,j):
            
            if i<0 or j<0 or i==len(grid) or j == len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            s = 0
            dir = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
            for x,y in dir:
                s+=dfs(i+x,j+y)
            return s+1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                m = max(m,dfs(i,j))
        return m
