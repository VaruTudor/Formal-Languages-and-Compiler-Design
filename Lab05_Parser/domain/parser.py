from domain.item import Item
from domain.state import State
import copy

from domain.table import Table

AUGMENTED_PRODUCTION_LHS = 'S`'


class Parser:
    """
    LR0 Parser
    """

    def __init__(self, grammar):
        self.grammar = grammar
        self.addAugmentedProduction()
        self.items = []
        self.computeInitialLr0Items()
        self.canonicalCollection = []
        self.table = Table(self.grammar.N + self.grammar.E)

    def addAugmentedProduction(self):
        """
        Create a new production S` -> S (start symbol) which is added as a first production to the set of productions.
        """
        productions = {AUGMENTED_PRODUCTION_LHS: [(self.grammar.S, -1)]}
        productions.update(self.grammar.P)
        self.grammar.P = productions

    def computeInitialLr0Items(self):
        """
        For each production create a new LR0 item and add it to the list of items. By creating a LR0 item, we mean adding
        the dot on the first position in the rhs before any symbol. In the Item object we abstract "." retaining only
        the position where it should be and not actually modifying the rhs.
        """
        for lhs in self.grammar.P:
            for rhs in self.grammar.P[lhs]:
                self.items.append(Item(lhs, rhs[0]))

    def closure(self, itemList):
        """
        For each item in the item list, if after dot there is a non-terminal, add it to the list of items and repeat the
        process.
        pseudocode:
        repeat
            for any [A -> α.Bβ] in C do
                for any B -> γ in P do
                    if [B -> .γ] 2/ C then
                        C = C U [B -> .γ]
                    end if
                end for
            end for
        until C stops changing
        :param itemList: a list of LR(0) items
        :return: the resulting state
        """
        items = itemList.copy()
        while True:
            itemsAtIterationStart = items.copy()
            for item in itemsAtIterationStart:
                if item.dotPosition == len(item.rhs):
                    # dot position is at the end
                    continue
                if item.getSymbolAfterDot() in self.grammar.N:
                    # non-terminal follows dot
                    for otherItem in self.items:
                        if otherItem.lhs == item.getSymbolAfterDot() and otherItem not in items:
                            items.append(otherItem)
            if itemsAtIterationStart == items:
                break
        if items[0].lhs == AUGMENTED_PRODUCTION_LHS:
            return State(items, len(self.canonicalCollection))
        return State(items, len(self.canonicalCollection))

    def isInCanonicalCollection(self, state):
        """
        For each existing state in the canonical collection, check if it has the same LR0 items as the given state.
        :param state: the state to be checked
        :return: True if found, otherwise False
        """
        for other in self.canonicalCollection:
            if state.items == other.items:
                return True
        return False

    def computeCanonicalCollection(self):
        """
        For each state s in the canonical collection, for each symbol X (in both terminals and non-terminals), check if
        goto(s,X) result is not an empty list nor exists already in the canonical collection and if so add it to the
        canonical collection
        pseudocode:
        repeat
            for any s in C do
                for any X in N U ß do
                    if goto(s,X) != ∅ and goto(s,X) not in C then
                        C = C U goto(s,X)
                    end if
                end for
            end for
        until C stops changing
        """
        # add initial state - closure of augmented production
        self.canonicalCollection.append(self.closure([self.items[0]]))
        while True:
            canonicalCollectionAtIterationStart = self.canonicalCollection.copy()
            for state in canonicalCollectionAtIterationStart:
                for symbol in self.grammar.N + self.grammar.E:
                    gotoResult = self.goto(state, symbol)
                    if gotoResult != [] and not self.isInCanonicalCollection(gotoResult):
                        self.canonicalCollection.append(gotoResult)
            if canonicalCollectionAtIterationStart == self.canonicalCollection:
                break

    def goto(self, state, symbol):
        """
        For each LR0 item in the state move the dot if the symbol follows it. Perform closure on the modified item.
        pseudocode:
        goto(s, X) = closure({[A → αX.β]|[A → α.Xβ] ∈ s})
        :param state: the state to be checked
        :param symbol: the symbol to be checked
        :return: closure of the updated items
        """
        items = []
        for item in state.items:
            # dot position is at the end
            if item.isDotAtTheEnd():
                continue
            if item.getSymbolAfterDot() == symbol:
                newItem = copy.deepcopy(item)
                newItem.moveDot()
                items.append(newItem)
        if items:
            gotoResult = self.closure(items)
            if gotoResult != [] and not self.isInCanonicalCollection(gotoResult):
                self.table.addSymbolToState(state, symbol, gotoResult)
            return gotoResult
        else:
            return []

    def computeTableActions(self):
        """
        For each state in the canonical collection add in the LR0 Table it's appropriate action
        """
        for state in self.canonicalCollection:
            item = state.items[0]
            if item.lhs == AUGMENTED_PRODUCTION_LHS and item.isDotAtTheEnd():
                self.table.addActionToState(state, 'acc     ')
            elif item.isDotAtTheEnd():
                reduceValue = -1
                for rhs in self.grammar.P[item.lhs]:
                    if item.rhs == rhs[0]:
                        reduceValue = rhs[1]
                self.table.addActionToState(state, 'reduce ' + str(reduceValue))

            else:
                self.table.addActionToState(state, 'shift   ')

    def printCanonicalCollection(self):
        result = ''
        for state in self.canonicalCollection:
            result += repr(state)
            result += '\n'
        print(result[:-1])

    def printLr0Table(self):
        print(self.table)
