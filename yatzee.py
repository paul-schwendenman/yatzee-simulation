#!/usr/bin/python


import random
import copy

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
    print '|\t|'.join([ppDice[dice][0] for dice in fivedice])
    print '|\t|'.join([ppDice[dice][1] for dice in fivedice])    
    print '|\t|'.join([ppDice[dice][2] for dice in fivedice])    
    print

# * * * * * * * * * * * * * * * *
# * Dice Helpers                *
# * * * * * * * * * * * * * * * *

def roll():
    return random.randrange(1,7)

def makeFiveDice():
    return [roll(), roll(), roll(), roll(), roll()]

def printFiveDice(fivedice):
    return ' '.join([str(dice) for dice in fivedice])
    
def selectiveReroll(fivedice, lst):
    new = copy.deepcopy(fivedice)
    for item in lst:
        new[item] = roll()
    return new

def allCombs(lst):
    if len(lst) == 1:
        'Base Case'
        all = [[lst[0]], []]
    else:
        small = allCombs(lst[1:])
        tall = [item + [lst[0]] for item in small]
        all = tall + small
        
    return all
        
        
def rollAgain(fivedice):
    all = [selectiveReroll(fivedice, comb) for comb in allCombs([0,1,2,3,4])]
    return all


def pickBest(all):
    scores = [scoreDice(dice) for dice in all]
    best = (lambda x: (all[scores.index(x)], x))(max(scores))
    best[0].sort()
    prettyPrint(best[0])
    print best[1]
    return best[0]
        

# * * * * * * * * * * * * * * * *
# * Tests                       *
# * * * * * * * * * * * * * * * *

def testDice(fivedice):
    print "running tests"
    count = testNumber(fivedice)
    print "1s: ", countAces(count)
    print "2s: ", countTwos(count)
    print "3s: ", countThrees(count)
    print "4s: ", countFours(count)
    print "5s: ", countFives(count)
    print "6s: ", countSixes(count)
    print
    print "3k: ", testThreeOfKind(fivedice, count)
    print "4k: ", testFourOfKind(fivedice, count)
    print "FH: ", testFullHouse(count)
    print "SS: ", testSmallStraight(fivedice)
    print "LS: ", testLargeStraight(fivedice)
    print "Yz: ", testYatzee(count)
    print "Ch: ", testChance(fivedice)

def scoreDice(fivedice):
    count = testNumber(fivedice)
    
    scores = [countAces(count),
              countTwos(count),
              countThrees(count),
              countFours(count),
              countFives(count),
              countSixes(count),
              testThreeOfKind(fivedice, count),
              testFourOfKind(fivedice, count),
              testFullHouse(count),
              testSmallStraight(fivedice),
              testLargeStraight(fivedice),
              testYatzee(count),
              testChance(fivedice)]
              
    return max(scores)

def testNumber(fivedice):
    return [len(filter(lambda (x): x==num, fivedice)) for num in range(1,7)]

def testNumbers(fivedice, lst):
    return 0 not in [item in fivedice for item in lst]

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
# * Main Function               *
# * * * * * * * * * * * * * * * *


def main():
    fivedice = makeFiveDice()
    fivedice.sort()
    prettyPrint(fivedice)
    print scoreDice(fivedice)
    
    #all = rollAgain(fivedice)    
    #all2 = [rollAgain(item) for item in all]
    #all3 = reduce(lambda x, y: x+y, all2)
    #print len(all3)
    #pickBest(all3)
    
    #pickBest(rollAgain(pickBest(all)))
    
    #prettyPrint(fivedice)
    #print scoreDice(fivedice)
    testDice(fivedice)

if __name__ == "__main__":
    main()
