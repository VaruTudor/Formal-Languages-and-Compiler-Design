import re
from domain.tokens import *


class Scanner:

    def __init__(self) -> None:
        self.cases = ["=+", "<+", ">+", "<=+", ">=+", "==+", "!=+", "=-", "<-", ">-", "<=-", ">=-", "==-", "!=-"]

    def getStringToken(self, line, index):
        """
        Finds the next token which is a string (between "").
        :param line: the current line from the program (a string)
        :param index: current position in line
        """
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\"':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def isPartOfOperator(self, char):
        """
        Checks if a character is part of an operator.
        :param char: the character to be checked
        """
        for operator in operators:
            if char in operator:
                return True
        return False

    def getOperatorToken(self, line, index):
        """
        Finds the next token which is an operator.
        :param line: the current line from the program (a string)
        :param index: current position in line
        """
        token = ''

        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        """
        Splits the line into tokens and adds them to a list.
        :param line: the current line from the program (a string)
        """
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                # operator check
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '\"':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in separators:
                # separator check
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    @staticmethod
    def isIdentifier(token):
        return re.match(identifier, token) is not None

    @staticmethod
    def isConstant(token):
        return re.match(constant, token) is not None
