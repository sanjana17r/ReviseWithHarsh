def serialize(root, A):
#Serialization by PreOrder Traversal
    if not root:
        A.append('#')
        return None
    A.append(root.data)
    serialize(root.left, A)
    serialize(root.right, A)
    #code here
    # i = 0
def deSerialize(A):
    if len(A) == 0:
        return
    val = A.pop(0)
    if val == '#':
        return None
    node = Node(val)
    node.left = deSerialize(A)
    node.right = deSerialize(A)
    return node
