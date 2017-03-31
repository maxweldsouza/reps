# ctci 4.5

def validate_bst(node):
    nmin = node.data, nmax = node.data, lvalid = True, rvalid = True
    if node.left:
        nmin, _, lvalid = validate_bst(node.left)
    if node.right:
        nmax, _, rvalid = validate_bst(node.right)
    if node.data < nmin:
        return (node.data, nmax, False)
    if node.data > nmax:
        return (nmin, node.data, False)
    return (nmin, nmax, lvalid and rvalid)
