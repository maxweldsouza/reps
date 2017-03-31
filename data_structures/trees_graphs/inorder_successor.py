# ctci 4.6

def inorder_successor(node):
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
    else:
        successor = node.parent
    return successor
