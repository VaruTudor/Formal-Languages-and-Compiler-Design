from domain import tokens


class FileReader:

    def __init__(self, filename):
        self.__filename = filename
        self.__tokens = []

    def openFile(self):
        return open(self.__filename, "r")

    def parseFile(self):
        fileStream = self.openFile()
        currentToken = ""

        for character in fileStream:
            if character not in tokens.separators:
                currentToken += character
            else:
                self.__tokens.append(currentToken)
                currentToken = ""

    def getTokens(self):
        return self.__tokens
