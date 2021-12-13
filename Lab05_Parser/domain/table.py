import copy

totalTableColumnSize = 18


def addSpaces(number):
    result = ''
    for _ in range(number):
        result += ' '
    return result


class Table:

    def __init__(self, symbols):
        self.actionsForStates = {}
        self.stateToStateMap = {}
        self.symbolsToStateDefault = {}
        for symbol in symbols:
            self.symbolsToStateDefault[symbol] = -1

    def addSymbolToState(self, fromState, symbol, toState):
        if fromState not in self.stateToStateMap.keys():
            symbolsToState = copy.deepcopy(self.symbolsToStateDefault)
            self.stateToStateMap[fromState] = symbolsToState
            if self.stateToStateMap[fromState][symbol] == -1:
                self.stateToStateMap[fromState][symbol] = toState.index
        else:
            if self.stateToStateMap[fromState][symbol] == -1:
                self.stateToStateMap[fromState][symbol] = toState.index

    def addActionToState(self, fromState, action):
        self.actionsForStates[fromState] = action

    def isActionToStateDefined(self, fromState):
        return fromState in self.actionsForStates.keys()

    def __repr__(self):
        result = '   | Action           |'
        for symbol in self.symbolsToStateDefault.keys():
            result += str(symbol)
            result += addSpaces(totalTableColumnSize - len(symbol))
            result += '|'
        for state in self.actionsForStates.keys():
            result += '\n'
            result += str(state.index)
            result += addSpaces(3 - len(str(state.index)))
            result += '|' + str(self.actionsForStates[state])
            result += addSpaces(totalTableColumnSize - len(str(self.actionsForStates[state])))
            result += '|'
            if state not in self.stateToStateMap.keys():
                for _ in self.symbolsToStateDefault.keys():
                    result += addSpaces(totalTableColumnSize)
                    result += '|'
            else:
                for symbol in self.stateToStateMap[state].keys():
                    if self.stateToStateMap[state][symbol] == -1:
                        result += addSpaces(totalTableColumnSize)
                        result += '|'
                    else:
                        result += str(self.stateToStateMap[state][symbol])
                        result += addSpaces(totalTableColumnSize - len(str(self.stateToStateMap[state][symbol])))
                        result += '|'
        return str(result)

    def __str__(self):
        return self.__repr__()
