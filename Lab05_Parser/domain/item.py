class Item:

    def __init__(self, lhs: str, rhs: str):
        self.lhs = lhs
        self.rhs = rhs
        self.dotPosition = 0

    def moveDot(self):
        self.dotPosition += 1

    def getSymbolAfterDot(self):
        return self.rhs[self.dotPosition]

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs and self.dotPosition == other.dotPosition

    def __repr__(self):
        representation = self.lhs + ' -> '
        for pos in range(0, self.dotPosition):
            representation += self.rhs[pos]
        representation += '.'
        for pos in range(self.dotPosition, len(self.rhs)):
            representation += self.rhs[pos]
        return representation

    def __str__(self):
        return self.__repr__()
