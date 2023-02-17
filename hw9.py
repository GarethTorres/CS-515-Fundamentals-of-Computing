def twoMaxes(L):
# takes in a two-dimensional list L and returns a list of lists. 
# The list return have two elements. The first is the max of each row, second is the max of each columns.
    max_of_each_row = list(map(max, L))
    max_of_each_columns = [ max(i) for i in zip( * L) ]
    return max_of_each_row, max_of_each_columns

L = [[1,2,6,5,8,4,6,4],[3,4,6,5,3,1,9,5]] 
print(twoMaxes(L))
#[[2, 4], [3, 4]]

def dictionaryCollector(L):
# takes in .a list L and returns a dictionary 
# The dictionary has two keys, ’int’ and ’string’, 
# ’int’ contains the sum of all elements in the list L 
# ’string’ has the value of all of the strings in L concatenated IN-ORDER. 
# Values of all other types in L should be ignored.
#    final_dictionary = dict('int'= , 'string')
    alist = []
    number = 0
    sentence = ''
    for i in L:
        if type(i) == int:
            number += i
        elif type(i) == str:
            alist.append(i)
    for j in alist:
        sentence += str(j)
    final_dictionary = {'int': number, 'string': sentence}
    return final_dictionary

L = [True, 1, 4, 5, 'hello', 10, '10', 'world']
d = dictionaryCollector(L)
print(d)
# {’int’: 20, ’string’: ’hello10world’}

def separateNumbers(L):
    if not L: 
        return [], []
    list_of_odd, list_of_even = separateNumbers(L[1:])
    
    if L[0] % 2: 
        return [L[0], * list_of_odd], list_of_even
    else:
        return list_of_odd, [L[0], * list_of_even]

# takes in a list of numbers L returns two lists, 
# the first one contains the odd numbers from the list
# the second one contains the even numbers. 
# This function MUST be written recursively.
inputList = [1,2,3,23,423,2,44,3,4,5,6,7,8,9,10] 
L = separateNumbers(inputList)
print(L) 
# [[1,3,5,7,9],[2,4,6,8,10]]

from math import pi
class Circle(object):
    def __init__(self,radius):
        self.radius = radius

    def __str__(self):
        return 'Radius: ' + str(self.radius)

    def area(self):
        return pi *self.radius * self.radius

class Sphere(Circle):
    def area(self):
        return 4 * pi * self.radius ** 2
    def volume(self):
        return 4/3 * pi * self.radius ** 3 

c = Circle(3)
s = Sphere(4)
print(c)
print(s)
print(c.area())
print(s.area())
print(s.volume())

import math
def preciseDivision(a,b):
# takes in two values, a and b 
# attempts to do a/b. 
# If there is division by 0, return float(math.inf). 
# If there is any other error, return None. 
# Otherwise, just do the division as normal.
    try:
        return a / b
    except ZeroDivisionError:
        return float(math.inf)
    except:
        return None

print(preciseDivision(9,8)) 
print(preciseDivision(-3,9)) 
print(preciseDivision(4,-3))
print(preciseDivision(0,8)) 
print(preciseDivision(9,0)) 
print(preciseDivision(98.123,1312.14))
print(preciseDivision('fas',33))
print(preciseDivision(333,'fff'))