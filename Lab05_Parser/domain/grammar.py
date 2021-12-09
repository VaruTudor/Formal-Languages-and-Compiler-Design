class Grammar:

    def __init__(self, N, E, P, S, isCFG):
        self.N = N
        self.E = E
        self.P = P
        self.S = S
        self.isCFG = isCFG

    @staticmethod
    def parseLine(line):
        afterEqual = line.strip().split('=')[1]
        withoutParenthesis = afterEqual.strip()[1:-1].strip()
        return [value.strip() for value in withoutParenthesis.split(',')]

    @staticmethod
    def fromFile(fileName):

        with open(fileName, 'r') as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = file.readline().split('=')[1].strip()
            rules = Grammar.parseLine(''.join([line for line in file]))
            P = Grammar.parseRules(rules)
            isCFG = Grammar.checkCFG(rules, N)
            return Grammar(N, E, P, S, isCFG)

    @staticmethod
    def parseRules(rules):
        result = {}
        index = 1

        for rule in rules:
            lhs, rhs = rule.split('->')
            lhs = [value.strip() for value in lhs.split('|')]
            rhs = [value.strip() for value in rhs.split('|')]

            for valueLhs in lhs:
                for value in rhs:
                    if valueLhs in result.keys():
                        result[valueLhs].append((value, index))
                    else:
                        result[valueLhs] = [(value, index)]
                    index += 1

        return result

    @staticmethod
    def checkCFG(rules, N):
        for rule in rules:
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            count = 0
            for element in lhs.split('|'):
                element = element.strip()
                if element in N:
                    count += 1
            if count > 1:
                return False
        return True

    def isNonTerminal(self, value):
        return value in self.N

    def getProductionsFor(self, nonTerminal):
        if self.isNonTerminal(nonTerminal):
            for key in self.P.keys():
                if key == nonTerminal:
                    return self.P[key]

    def getProductions(self):
        return [self.getProductionsFor(nonTerminal) for nonTerminal in self.N]

    def getProductionAsPair(self, index):
        for key, value in self.P.items():
            for rhs in value:
                if rhs[1] == index:
                    return key, rhs[0]

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }'
