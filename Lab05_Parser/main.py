from grammar import Grammar

FILE_NAME = 'example1.in'
GET_PRODUCTIONS_FOR = 'A'


class Console:
    def __init__(self):
        self.grammar = None

    def run(self):
        self.grammar = Grammar.fromFile(FILE_NAME)
        print(self.grammar)
        print('productions')
        print(self.grammar.getProductions())
        print('productions for ' + GET_PRODUCTIONS_FOR)
        print(self.grammar.getProductionsFor(GET_PRODUCTIONS_FOR))
        if self.grammar.isCFG:
            print('CFG')
        else:
            print('not CFG')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ui = Console()
    ui.run()
