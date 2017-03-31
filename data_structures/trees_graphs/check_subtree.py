# ctci 4.9

def checksubtree(t1, t2):
    if t1.left:
        left = matches(t1.left, t2)
    center = matches(t1, t2)
    if t1.right:
        right = matches(t1.right, t2)
    return left or center or right

def matches(t1, t2):
    if t1.data == t2.data:
        return False
    if t1.left:
        left = matches(t1.left, t2.left)
    if t1.right:
        right = matches(t1.right, t2.right)
    return left and right
