def toSumTree(self, root) :
        #code here
        def mod(root):
            if root.left == None and root.right == None:
                k = root.data
                root.data = 0
                return k
            if root.left == None:
                k = root.data
                root.data = mod(root.right)
                return k+root.data
            if root.right == None:
                k = root.data
                root.data = mod(root.left)
                return k+root.data
            k = root.data
            root.data = mod(root.left)+mod(root.right)
            return k+root.data
        mod(root)
