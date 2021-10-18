import re

from domain.Scanner import Scanner
from domain.SymbolTable import ST
from domain.ProgramInternalForm import PIF
from domain.tokens import *

ST_SIZE = 10


class TestScanner:
    def __init__(self):
        self.st = ST(ST_SIZE)
        self.pif = PIF()
        self.scanner = Scanner()

    def testBasic(self):
        scanner = Scanner()
        lineSMALL = "abc=b and h{a}==df;o=\"da\""
        print(lineSMALL)
        print(scanner.tokenize("abc=b and h{a}==df;o=\"da\""))

    def testFile(self, filename):
        exceptionMessage = ""

        with open(filename, 'r') as file:
            numberOfCurrentLine = 0
            for line in file:
                numberOfCurrentLine += 1
                tokens = self.scanner.tokenize(line.strip())
                for i in range(len(tokens)):
                    if tokens[i] in keywords + separators + operators:
                        if tokens[i] == ' ':
                            continue
                        self.pif.add(tokens[i], (-1, -1))
                    elif tokens[i] in self.scanner.cases and i < len(tokens) - 1:
                        if re.match("[1-9]", tokens[i + 1]):
                            self.pif.add(tokens[i][:-1], (-1, -1))
                        else:
                            exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                                numberOfCurrentLine) + "\n"
                    elif Scanner.isIdentifier(tokens[i]):
                        self.pif.add("id", self.st.add(tokens[i]))
                    elif Scanner.isConstant(tokens[i]):
                        self.pif.add("const", self.st.add(tokens[i]))
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            numberOfCurrentLine) + "\n"

        with open('st.out', 'w') as writer:
            writer.write(str(self.st))

        with open('pif.out', 'w') as writer:
            writer.write(str(self.pif))

        if exceptionMessage == "":
            print("Lexically correct")
        else:
            print(exceptionMessage)

    def testP1(self):
        self.testFile('p1.txt')

    def testP2(self):
        self.testFile('p2.txt')

    def testP3(self):
        self.testFile('p3.txt')

    def testP1Err(self):
        self.testFile('p1err.txt')
