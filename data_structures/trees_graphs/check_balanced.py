# ctci 4.4

def check_balanced(node):
    left = 0, right = 0
    if node.left:
        left, _ = check_balanced(node.left)
    if node.right:
        right,_ = check_balanced(node.right)
    return (max(left, right+1), abs(left-right) <= 1)
