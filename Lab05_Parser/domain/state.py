class State:

    def __init__(self, items, index):
        self.items = items
        self.index = index

    def add(self, item):
        self.items.append(item)

    def __repr__(self):
        result = 'S' + str(self.index) + '( '
        result += str(self.items)
        result += ' )'
        return result

    def __str__(self):
        return self.__repr__()
