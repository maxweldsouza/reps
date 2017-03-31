# ctci 2.1
#done

from collections import defaultdict

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

def remove_dups(node):
    seen = defaultdict(int)
    while node:
        if seen[node.next.data]:
            node.next = node.next.next
            continue
        else:
            seen[node.next.data] += 1
        node = node.next
    return

def remove_dups_no_buffer(node):
    while node:
        fast = node
        while fast.next:
            if fast.next.data == node.data:
                fast.next = fast.next.next
                continue
            fast = fast.next
        node = node.next
    return

x = Node(3)
x.append(4).append(3).append(1).append(5).append(5)
print x
remove_dups_no_buffer(x)
print x
