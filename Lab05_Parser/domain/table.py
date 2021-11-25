import copy


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
            self.stateToStateMap[fromState][symbol] = toState.index
        else:
            self.stateToStateMap[fromState][symbol] = toState.index

    def addActionToState(self, fromState, action):
        self.actionsForStates[fromState] = action

    def __repr__(self):
        result = ' | Action     |'
        for symbol in self.symbolsToStateDefault.keys():
            result += str(symbol) + '   |'
        for state in self.actionsForStates.keys():
            result += '\n'
            result += str(state.index) + '| ' + str(self.actionsForStates[state]) + '   |'
            if state not in self.stateToStateMap.keys():
                for _ in self.symbolsToStateDefault.keys():
                    result += '    |'
            else:
                for symbol in self.stateToStateMap[state].keys():
                    if self.stateToStateMap[state][symbol] == -1:
                        result += '    |'
                    else:
                        result += str(self.stateToStateMap[state][symbol]) + '   |'
        return str(result)

    def __str__(self):
        return self.__repr__()
