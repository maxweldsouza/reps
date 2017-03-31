# ctci 16.20

class Trie(object):
    def __init__(self, key=None):
        self.children = []
        self.key = key
        self.values = []


    def match(self, digits):
        if len(digits) == 1:
            for child in self.children:
                if child.key == digits[0]:
                    return child.allvalues()
            return []
        else:
            for child in self.children:
                if child.key == digits[0]
                    return child.match(digits[1:])
                else:
                    return []

    def all_values(self):
        for i in self.values:
            yield i
        for child in self.children:
            for value in child.values():
                yield value

    def add(self, word, depth=0):
        self.key = lettertodigit(word[depth])
        if depth == len(word) - 1:
            self.values.append(word)
        else:
            for child in self.children:
                if child.key == word[depth]:
                    child.add(word, depth=depth+1)
                    return
            child = Trie(word[depth])
            child.add(word, depth=depth+1)

    @staticmethod
    def lettertodigit(letter):
        key = '22233344455566677778899999'
        return key[ord(letter.tolower())]
