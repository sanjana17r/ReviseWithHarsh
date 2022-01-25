def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = { i:[] for i in range(numCourses) }
        for i,j in prerequisites:
                dic[i].append(j)
        res = []
        visited = set()
        added = set()
        def dfs(num):
            if dic[num] == []:
                if num not in added:
                    res.append(num)   
                    added.add(num)
                return True
            if num in visited:
                return False
            visited.add(num)
            for n in dic[num]:
                if dfs(n) == False:
                    return False
            visited.remove(num)
            dic[num] = []
            if num not in added:
                res.append(num)   
                added.add(num)
            return True
        
        for i in range(numCourses):
            if (dic[i] == []) or dfs(i):
                if i not in added:
                    res.append(i)
                    added.add(i)
            else:
                return []
        return res
