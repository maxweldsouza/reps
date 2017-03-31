# ctci 17.20

import operator
class Heap(object):
    def __init__(self, minheap=True):
        self.items = []
        self.minheap = minheap

    @staticmethod
    def children(i):
        first = 2*i + 1
        return [x for x in [first, first+1] if x < len(self.items)]

    @staticmethod
    def parent(i):
        return (i - 1) / 2

    def __len__(self):
        return len(self.items)

    def siftup(self):
        i = len(self.items) - 1
        op = operator.gt if self.minheap else operator.lt
        while i >= 0:
            p = Heap.parent(i)
            if op(arr[i], arr[p]):
                arr[i], arr[p] = arr[p], arr[i]
            i = p

    def append(self, item):
        self.items.append(item)
        self.siftup()

    def root(self):
        return self.items[0]

    def extractroot(self):
        root = self.items[0]
        if len(self.items) > 1:
            self.items[0] = self.items[-1]
            self.items.pop()
            self.siftdown()
        else:
            return None

    def siftdown(self):
        if len(self.items) == 0:
            return
        i = 0
        children = Heap.children(i)
        while children:
            children = Heap.children(i)
            for child in children:
                if self.items[i] < self.items[child]
                    self.items[i], self.items[child] = self.items[child], self.items[i]
                    i = child
                    continue

class ContinuousMedian(object):
    def __init__(self):
        self.minheap = Heap(minheap=True)
        self.maxheap = Heap(minheap=False)

    def append(self.item):
        self.minheap.append(item)
        self.balance()

    def balance(self):
        if len(self.minheap) - len(self.maxheap) > 1:
            x = self.minheap.pop()
            self.maxheap.append(x)
        elif len(self.minheap) - len(self.maxheap) < -1:
            x = self.maxheap.pop()
            self.maxheap.append(x)

    def median(self):
        if len(self.minheap) > len(self.maxheap):
            return self.minheap.root()
        else:
            return self.maxheap.root()
