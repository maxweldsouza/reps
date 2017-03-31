# ctci 2.3
#done

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

def delete_middle_node(node):
    if node.next:
        node.data = node.next.data
        node.next = node.next.next
    else:
        node.data = None
        node.dummy = True
    return

x = Node(3)
x.append(4).append(3).append(1).append(5).append(5)
print x
delete_middle_node(x.next.next.next)
print x
