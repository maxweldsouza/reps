# ctci 4.8

def first_common_ancestor(node, a, b):
    if node == a:
        return (None, True, False)
    if node.left:
        _, aleft, bleft = first_common_ancestor(node.left, a, ab)
    if node.right:
        _, aright, bright = first_common_ancestor(node.right, a, b)
    if (aleft and bright) or (bleft and aright):
        return (node, True, True)
    else:
        return (None, aleft or aright, bleft or bright)
