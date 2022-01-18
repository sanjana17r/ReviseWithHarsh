def countSubtreesWithSumX(root, x):
    global count
    count = 0
    
    def dfs(root):
        global count
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        if root.left:
            root.data += root.left.data
        if root.right:
            root.data += root.right.data
        if root.data == x:
            count+=1
    
    dfs(root)
    return count
