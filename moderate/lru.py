# ctci 16.25

class LRU(object):
    def __init__(self, maximum):
        self.maximum = maximum
        l = DoublyLinkedList()
        d = {}

    def add(self, key, value):
        node = Node(value)
        d[key] = node
        if len(l) == self.max:
            l.removelast()
        l.append(node)

    def get(self, key):
        if key in d:
            node = d[key]
            node.movetotop()
            return node.value
        else:
            raise KeyError()

    def set(self, key, value):
        if key in d:
            node = d[key]
            node.value = value
        else:
            self.add(key, value)
