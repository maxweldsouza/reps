class BSTree(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BSTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right= BSTree(data)

    def __repr__(self, level=1):
        result = str(self.data) + ' '
        if self.left:
            result += '\n' + level * '    ' + self.left.__repr__(level=level+1)
        if self.right:
            result += '\n' + level * '    ' + self.right.__repr__(level=level+1)
        return result

    def search(self, data):
        if self is None:
            return self
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

def inorder(node):
    if node.left is not None:
        for left in inorder(node.left):
            yield left
    yield node.data
    if node.right is not None:
        for right in inorder(node.right):
            yield right




tree = BSTree(3)
tree.insert(1)
tree.insert(2)
tree.insert(5)
tree.insert(4)
print tree
print tree.search(1)
print list(inorder(tree))
