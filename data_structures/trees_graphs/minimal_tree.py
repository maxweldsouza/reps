# ctci 4.2

class Tree(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def minimal_tree(arr, left, right):
    if left == right:
        node = Node(arr[left])
    elif right - left == 1:
        node = Node(arr[left])
        node.right = Node(arr[right])
    else:
        middle = (left + right) / 2
        node = Node(arr[middle])
        node.left = minimal_tree(arr, 0, middle-1)
        node.right = minimal_tree(arr, middle+1, right)
    return node
