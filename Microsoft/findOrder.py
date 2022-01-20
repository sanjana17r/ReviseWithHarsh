def dfs(self,graph, visited, u, result):
        visited[u] = True
        
        for j in graph.get(u, []):
            if visited[j] is False:
                self.dfs(graph, visited, j, result)
        result.append(u)

    def findOrder(self,alien_dict,n,k):
        # code here
        # return the string containing all k characters in correct order
        graph = {}
        visited = {}
        alpha = []
        
        for i in range(1, len(alien_dict)):
            for j in range(min(len(alien_dict[i-1]), len(alien_dict[i]))):
                if alien_dict[i-1][j] != alien_dict[i][j]:
                    graph.setdefault(alien_dict[i-1][j], [])
                    graph[alien_dict[i-1][j]].append(alien_dict[i][j])
                    break
        
        for word in alien_dict:
            for letter in word:
                if letter not in visited:
                    visited[letter] = False
                    # Alpha is used here to preserve order of letters.
                    # Ordered dict can also be used for visited.
                    alpha.append(letter)
        
        result = []
        for i in alpha:
            if visited[i] is False:
                self.dfs(graph, visited, i, result)
        result.reverse()
        return result
