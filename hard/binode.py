# ctci 17.12

class BiNode(object):
    def __init__(self):
        self.next = None
        self.prev = None

def treeToLinkedList(node):
    if node.prev:
        treeToLinkedList(node.prev)
        first = node.prev
        while first:
            first = first.prev
        node.prev = first
    if node.next:
        treeToLinkedList(node.next)

        last = node.next
        while last:
            last = last.next
        node.next = last
