class PIF:
    def __init__(self):
        self.__items = []

    def add(self, token, pos):
        self.__items.append((token, pos))

    def __str__(self):
        result = ""
        for pair in self.__items:
            result += pair[0] + " - " + str(pair[1]) + "\n"
        return result
