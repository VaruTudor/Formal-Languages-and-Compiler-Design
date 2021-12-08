from domain.grammar import Grammar
from domain.parser import Parser

FILE_NAME = 'g3.txt'
GET_PRODUCTIONS_FOR = 'A'


def printBr():
    print('-----------------------------------------------------------------------------------------------------------')


class Console:
    def __init__(self):
        self.grammar = None
        self.parser = None

    def run(self):
        self.grammar = Grammar.fromFile(FILE_NAME)
        printBr()
        print('Non-terminals and Terminals:')
        print(self.grammar)
        printBr()
        print('Productions:')
        print(self.grammar.P)
        printBr()
        print('Productions for ' + GET_PRODUCTIONS_FOR + ':')
        print(self.grammar.getProductionsFor(GET_PRODUCTIONS_FOR))
        printBr()
        if self.grammar.isCFG:
            print('The grammar is CFG')
        else:
            print('The grammar is not CFG')
        printBr()
        print('Canonical Collection:')
        self.parser = Parser(grammar=self.grammar)
        self.parser.computeCanonicalCollection()
        self.parser.printCanonicalCollection()
        printBr()
        print('LR0 Table:')
        self.parser.computeTableActions()
        self.parser.printLr0Table()
        printBr()
        print('Parsing sequence: abbc')
        self.parser.parseSequence('abbc')
        printBr()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ui = Console()
    ui.run()
