def connect(self, root):
        que = []
        que.append(root)
        while que :
            l = len(que)
            for i in range(len(que)):
                temp = que.pop(0)
                l-=1
                if l == 0 :
                    temp.nextRight= None
                else :
                    temp.nextRight = que[0]
                if temp.left != None :
                    que.append(temp.left)
                if temp.right != None :
                    que.append(temp.right)
