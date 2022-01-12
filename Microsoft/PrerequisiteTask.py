def isPossible(self,N,prerequisites):
        graph = [[] for _ in range(N)]
        visit = [0 for _ in range(N)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(N):
            if not dfs(i):
                return False
        return True
