class Trie(object):
    def __init__(self, key):
        self.key = ord(key) if key else 0
        self.children = []
        self.no = 1

    def add(self, word):
        word = word
        current = self
        while True:
            if len(word) > 1:
                head, tail = word[0], word[1:]
            else:
                head = word
                tail = ''
            if len(word) > 0:
                found = False
                word = tail
                for node in current.children:
                    if chr(node.key) == head:
                        current = node
                        current.no += 1
                        found = True
                if not found:
                    child = Trie(head)
                    current.children.append(child)
                    current = child
            else:
                return

    def find(self, partial):
        current = self
        partial = partial
        while True:
            if len(partial) > 1:
                head, tail = partial[0], partial[1:]
            elif len(partial) == 0:
                return current.no
            else:
                head = partial
                tail = ''
            found = False
            for child in current.children:
                if chr(child.key) == head:
                    current = child
                    partial = tail
                    found = True
            if not found:
                return 0
        return 0

    def __repr__(self, level=0):
        result = chr(self.key) + '(' + str(self.no) + ')'
        for node in self.children:
            result += '\n' + '    ' * level + node.__repr__(level=level+1)
        return result

trie = Trie('')
trie.add('hack')
trie.add('hackerrank')


print trie
print trie.find('hac')
print trie.find('hak')
