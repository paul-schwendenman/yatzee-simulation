#!/usr/bin/python


import random

# * * * * * * * * * * * * * * * *
# * Dice Class                  *
# * * * * * * * * * * * * * * * *

class Dice():
    def __init__(self):
        self.roll()
        
    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        return self.value + other.value
    
    def __radd__(self, num):
        return num + self.value
        
    def __lt__(self, other):
        return self.value < other.value

    def roll(self):
        self.value = random.randrange(1,7)

# * * * * * * * * * * * * * * * *
# * Dice Pretty Print           *
# * * * * * * * * * * * * * * * *

ppOne = ["     ", "  *  ", "     "]
ppTwo = ["*    ", "     ", "    *"]
ppThree = ["*    ", "  *  ", "    *"]
ppFour = ["*   *", "     ", "*   *"]
ppFive = ["*   *", "  *  ", "*   *"]
ppSix = ["*   *", "*   *", "*   *"]

ppDice = [None, ppOne, ppTwo, ppThree, ppFour, ppFive, ppSix]

def prettyPrint(fivedice):
    print
    print '|\t|'.join([ppDice[dice.value][0] for dice in fivedice])
    print '|\t|'.join([ppDice[dice.value][1] for dice in fivedice])    
    print '|\t|'.join([ppDice[dice.value][2] for dice in fivedice])    
    print

# * * * * * * * * * * * * * * * *
# * Dice Helpers                *
# * * * * * * * * * * * * * * * *

def makeFiveDice():
    return [Dice(), Dice(), Dice(), Dice(), Dice()]

def printFiveDice(fivedice):
    return ' '.join([str(dice) for dice in fivedice])

# * * * * * * * * * * * * * * * *
# * Tests                       *
# * * * * * * * * * * * * * * * *

def testDice(fivedice):
    print "running tests"
    count = testNumber(fivedice)
    print countAces(count)
    print countTwos(count)
    print countThrees(count)
    print countFours(count)
    print countFives(count)
    print countSixes(count)
    print
    print testThreeOfKind(fivedice, count)
    print testFourOfKind(fivedice, count)
    print testFullHouse(fivedice)
    print testSmallStraight(fivedice)
    print testLargeStraight(fivedice)
    print testYatzee(count)
    print testChance(fivedice)

def testNumber(fivedice):
    return [len(filter(lambda (x): x.value==num, fivedice)) for num in range(1,7)]

def testNumbers(fivedice, lst):
    dice = [die.value for die in fivedice]
    return 0 not in [item in dice for item in lst]

def getSum(fivedice):
    return reduce(lambda x, y: x + y, fivedice)

def countAces(count):
    return count[0]

def countTwos(count):
    return count[1] * 2

def countThrees(count):
    return count[2] * 3

def countFours(count):
    return count[3] * 4

def countFives(count):
    return count[4] * 5

def countSixes(count):
    return count[5] * 6

def testThreeOfKind(fivedice, count):
    if (3 in count):
        return getSum(fivedice)
    return 0
    #return [num >= 3 for num in count]

def testFourOfKind(fivedice, count):
    if (4 in count):
        return getSum(fivedice)
    return 0
    #return [num >= 4 for num in count]

def testFullHouse(count):
    if (3 in count) and (2 in count):
        return 25
    return 0

def testSmallStraight(fivedice):
    if testNumbers(fivedice, [1, 2, 3, 4]) or \
       testNumbers(fivedice, [2, 3, 4, 5]) or \
       testNumbers(fivedice, [3, 4, 5, 6]):
        return 30
    return 0

def testLargeStraight(fivedice):
    if testNumbers(fivedice, [1, 2, 3, 4, 5]) or \
           testNumbers(fivedice, [2, 3, 4, 5, 6]):
        return 40
    return 0
    #return ((count[0] == 0) or (count[5] == 0)) and (max(count) == 1)
    
def testYatzee(count):
    if (5 in count):
        return 50
    return 0
    #return [num == 5 for num in count]

def testChance(fivedice):
    return getSum(fivedice)


# * * * * * * * * * * * * * * * *
# * Main Funstion               *
# * * * * * * * * * * * * * * * *


def main():
    fivedice = makeFiveDice()

    prettyPrint(fivedice)
    print printFiveDice(fivedice)
    fivedice.sort()
    prettyPrint(fivedice)
    print printFiveDice(fivedice)    

    testDice(fivedice)

if __name__ == "__main__":
    main()
