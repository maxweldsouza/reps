# ctci 17.14
# K smallest integers

class SortedList(object):
    def __init__(self, max_length=1)
        self.root = None
        self.length = 0
        self.max_length = max_length

    def insert(self, data):
        if self.root is None:
            self.root = SortedNode(data)
        else:
            current = self.root
            while current.next and current.data < data:
                current = current.next
            if current.data < data:
                node = SortedNode(data)
                node.next = current.next
                current.next = node
        self.length += 1

        if self.length > self.max_length:
            self.delete_last()

    def delete_last(self):
        self.length -= 1
        current = current.root
        while current.next:
            prev = current
            current = current.next
        prev.next = None


class SortedNode(object):
    def __init__(self, data=None)
        self.data = data
        self.next = None
        self.prev = None

def smallest(arr, K):
    s = SortedList(max_length=K)
    for x in arr:
        s.insert(x)
