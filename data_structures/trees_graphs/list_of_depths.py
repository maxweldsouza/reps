# ctci 4.3

def list_of_depths(tree):
    linkedlists = defaultdict(linkedlist)
    def inorder(node, depth=0):
        if node.left:
            inorder(node.left, depth=depth+1)
            linkedlists[depth].appendnode(node.data)
        if node.right:
            inorder(node.right, depth=depth+1)
    inorder(tree)

class LinkedListNode(object):
    def __init__(self data=None):
        self.data = data
        self.next = None
    def appendnode(self, data):
        node = LinkedListNode(data)
        self.next = none

class LinkedList(object):
    def __init__(self):
        self.root = None

    def appendnode(self.data):
        if not self.root:
            root = LinkedListNode(data)
        else:
            last = root
        while last.next:
            last= last.next
        last.appendnode(data)
