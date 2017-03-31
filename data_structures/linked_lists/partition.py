# ctci 2.4
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append(self, data):
        new = Node(data)
        self.next = new
        return new

    def __repr__(self):
        current = self
        result = [str(current.data)]
        while current.next:
            current = current.next
            result.append(str(current.data))
        return ''.join(result)

def partition(node, partition):
    small = linkedlist()
    big = linkedlist()

    if small.data:
        last = small
        while last.next:
            last = last.next
        if big.data:
            last.next = big
            return small
        else:
            return small
        elif big.data:
            return big
        else:
            return None

x = Node(3)
x.append(4).append(3).append(1).append(5).append(5)
print x
delete_middle_node(x.next.next.next)
print x
