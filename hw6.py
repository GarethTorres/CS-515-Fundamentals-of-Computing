def spiral(L):
    row = 0 
    column = -1
    indm = 1 
    indn = 0
    rows = len(L)
    columns = len(L[0])
    numbersofturns = 0
    timetoturn = verticalsteps = columns 
    horizontalsteps = rows - 1
    for i in range(rows * columns):
        row += indn 
        column += indm
        print (L[row][column]),
        if i == timetoturn - 1:
            numbersofturns += 1
            indm, indn = -indn, indm 
            if numbersofturns % 2 == 0 :
                horizontalsteps -= 1
                timetoturn += verticalsteps
            elif numbersofturns % 2 != 0 :
                verticalsteps -= 1
                timetoturn += horizontalsteps
                
print(spiral([[1,2,3],[4,5,6],[7,8,9]]))


def inverter(D) :
   newdict = {}
   for key, value in D.items():
      if value not in newdict:
          newdict[value] = key
      else:
          if type(newdict[value]) is not list:
            newdict[value]=[newdict[value],key]
          else:
            newdict[value].append(key)
   return newdict
print(inverter({1:'a', 2:'b', 3:'c'}))
print(inverter({1:'a', 2:'a', 3:'a',4:'b'}))

def matrixMultiply(A,B) :
    result = [[sum( m * n for m , n in zip(rowofA , columnofB)) 
                          for columnofB in zip(*B)] 
                          for rowofA in A]
    return result
print(matrixMultiply([[1,2,3],[4,5,6]],[[1,2],[3,4],[5,6]]))

def twoSum(L, t):
    sum = []
    newdict = {}
    for i in range(len(L)):
        secondnumber = t - L[i]
        if secondnumber in newdict:
            sum = (L[i],secondnumber)
            return sum
        newdict[L[i]] = L[i]
print(twoSum([1,2,3,4,5], 4))
print(twoSum([1,2,2,3,4,5], 4))