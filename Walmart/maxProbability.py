def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dic = {}
        suc = {}
        vis = set()
        for i in range(len(edges)):
            suc[(edges[i][0], edges[i][1])] = succProb[i]
            suc[(edges[i][1], edges[i][0])] = succProb[i]
        # print(suc)
        for i,j in edges:
            if i not in dic:
                dic[i] = [j]
            else:
                dic[i].append(j)
            if j not in dic:
                dic[j] = [i]
            else:
                dic[j].append(i)

        def dfs(p,i):
            if i in vis:
                return 0
            if i == end:                    
                return suc[(p,i)]
            vis.add(i)
            k = dic[i]
            cur = 0
            for j in k:
                cur = max(cur,dfs(i,j)*suc[(i,j)])
            vis.remove(i)
            return cur
        
        return dfs(start,start)
