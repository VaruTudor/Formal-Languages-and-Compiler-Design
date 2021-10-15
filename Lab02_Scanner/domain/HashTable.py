from collections import deque


class HashTable:
    def __init__(self, size):
        """
        For each position we'll store a deque ( implemented as a double ended linked list)
        and so if two elements hash to the same value they are chained to it's respective deque
        :param size: how positions will be in the hash table
        """
        self.__size = size
        self.__items = [deque() for _ in range(size)]

    def hash(self, key):
        """
        Modular hashing, the hash function is simply h(k) = k mod m for some m - size.
        k is computed as sum of all ASCII values of key's characters.
        The return value is an integer hash code generated from the input (key).
        :param key: input token
        :return: the value of the hash function
        """
        total_sum = 0
        for character in key:
            total_sum += ord(character)
        return total_sum % self.__size

    def add(self, key):
        if self.contains(key):
            return self.getPosition(key)
        self.__items[self.hash(key)].append(key)
        return self.getPosition(key)

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    def __str__(self) -> str:
        result = "ST\n"
        for i in range(self.__size):
            result = result + str(i) + "-" + str(self.__items[i]) + "\n"
        return result

    def getPosition(self, key):
        listPosition = self.hash(key)
        listIndex = 0
        for item in self.__items[listPosition]:
            if item != key:
                listIndex += 1
            else:
                break
        return listPosition, listIndex
