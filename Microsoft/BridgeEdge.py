def isBridge(self, V, adj, c, d):
        vis = [0]*V
        # code here
        def dfs(i,adj,c,d):
            vis[i]=1
            for x in adj[i]:
                if i == c and x == d:
                    continue
                if not vis[x]:
                    dfs(x,adj,c,d)
            return 0
        dfs(c,adj,c,d)
        if vis[d]:
            return 0
        return 
