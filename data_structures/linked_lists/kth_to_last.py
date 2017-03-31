# ctci 2.2
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
        return ' '.join(result)

def kthtolast(node, k):
    i = 0
    result = node
    while node:
        if i == k:
            if node.next:
                node = node.next
                result = result.next
            else:
                return result
        else:
            i += 1
            node = node.next
    return None

x = Node(3)
x.append(4).append(3).append(1).append(5).append(5)
print kthtolast(x, 3)
