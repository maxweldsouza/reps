# ctci 16.26

from __future__ import division
import operator
from collections import OrderedDict

class DoublyLinkedList(object):
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data

    def append(self, data):
        current = self
        while current:
            current = current.next
        node = DoublyLinkedList(data)
        current.next = node
        node.prev = current

def calculator(exp):
    lst = list(exp)

    if len(lst) == 0:
        raise Error('Invalid input')

    linkedlist = DoublyLinkedList(lst[0])
    for x in lst[1:]:
        linkedlist.append(x)

    ops = OrderedDict()
    ops['*'] = operator.mul
    ops['/'] = operator.truediv
    ops['+'] = operator.add
    ops['-'] = operator.sub

    for op in ops:
        node = linkedlist
        while node:
            if node.data == op:
                result = ops[op](node.prev.data, node.next.data)
                node.prev.data = result
                node.prev.next = node.next.next

            node = node.next

    return linkedlist.data

print calculator('3')
print calculator('2*3+5')
print calculator('2*3+5/6*3+15')
