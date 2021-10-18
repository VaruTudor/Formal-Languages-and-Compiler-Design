from domain.HashTable import HashTable
from tests import testHashTable, testScanner
from tests.testScanner import TestScanner

RUN_TESTS = True

if __name__ == '__main__':
    if RUN_TESTS:
        # testHashTable.testBasic()

        testScanner = TestScanner()
        # testScanner.testBasic()
        # testScanner.testP1()
        # testScanner.testP2()
        testScanner.testP3()
        # testScanner.testP1Err()
