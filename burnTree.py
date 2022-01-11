def minTime(self, root,target):
        # code here
        burned = set()
        parent = {}
        child={}
        q = deque()
        q.append(root)
        while(q):
            size = len(q)
            while(size):
                ele = q.popleft()
                if ele.left:
                    if ele.left.data in parent:
                        parent[ele.left.data].append(ele.data)
                    else:
                        parent[ele.left.data] = [ele.data]
                    if  ele.data in child:
                        child[ele.data].append(ele.left.data)
                    else:
                        child[ele.data] = [ele.left.data]
                    q.append(ele.left)
                if ele.right:
                    if ele.right.data in parent:
                        parent[ele.right.data].append(ele.data)
                    else:
                        parent[ele.right.data] = [ele.data]
                    if  ele.data in child:
                        child[ele.data].append(ele.right.data)
                    else:
                        child[ele.data] = [ele.right.data]
                    q.append(ele.right)
                size -= 1        
        time = 0
        burned.add(target)
        q2 = deque()
        q2.append(target)
        while(q2):
            time+=1
            size = len(q2)
            while(size):
                node = q2.popleft()
                burned.add(node)
                if node in parent:
                    currpar = parent[node]
                    for par in currpar:
                        if par not in burned:
                            q2.append(par)
                if node in child:
                    currchild = child[node]
                    for ch in currchild:
                        if ch not in burned:
                            q2.append(ch)
                size-=1
        return time-1
