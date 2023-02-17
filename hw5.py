def runningAverage(L):
    # Write a function runningAverage(L) which takes in a list L #
    # returns a new list where at each index n is the running average up to n in the original list. #
    sumofall = 0
    meanlist = []
    for i in range(len(L)) :
        sumofall += L[i]
        meanlist.append(sumofall / (i+1))
    return meanlist
test1 = runningAverage([1,2,3,4,5])
print(test1)

def double(n):
    return 2 * n

def isEven(n):
    return n % 2 == 0

def customMap(f,L) :
    # customMap and customFilter which take in a function f and a list L
    # replicate the behavior of map and filter respectively.
    doublelist = []
    for i in L:
        doublelist.append(f(i))
    return doublelist
test22 = customMap(double, [1,2,3])
print(test22)

def customFilter(f,L) :
    evennumber = []
    for i in L :
        if f(i) != False :
            evennumber.append(i)
    return evennumber
test333 = customFilter(isEven,[1,2,3])
print(test333)

def removeAdjDuplicates(L) :
    # Write a function called removeAdjDuplicates(L) #
    # removes adjacent duplicates from the input list. #
    compareobj = L[0]
    numberindex = 1
    while numberindex < len(L):
        if L[numberindex] == compareobj:
            del L[numberindex]
        else:
            compareobj = L[numberindex]
            numberindex = numberindex + 1
    return L
test4444 = removeAdjDuplicates([1,1,2,3,4,1,5,5,5,5,5])
print(test4444)

def flatten(L):
    # Write a function called flatten(L) #
    # which takes in a list which may contain other lists, #
    # flattens it so that it has a depth of 1. #
    flattenlist = []
    def loop(n):
        for i in n:
            if isinstance(i,list):
                loop(i)
            else:
                flattenlist.append(i)
    loop(L)
    return flattenlist
test55555 = flatten([1,2,[3,4],5,[6,[7,8]]])
print(test55555)