from cs515 import map, filter

def cToF(t):
  return t * 9/5+32
print(cToF(10))

def fToC(t):
  return (t - 32) * 5 / 9
print(fToC(50))

def addTwoNumbers(a,b):
  return a+b
print(addTwoNumbers(1,2))

def multiplyTwoNumbers(a,b):
  return a*b
print(multiplyTwoNumbers(3,4))

def calculate(a):
  return addTwoNumbers(multiplyTwoNumbers(a,a),2)
print(multiplyTwoNumbers(5,5)+2)

def longStrings(L):
  return len(L)> 5
L=['s','abj','adkkff','sd','afafasfa']
print(filter(longStrings, L))

def doubleStrings(L):
  return L * 2
L=['s','aa','cccc','cc']
print(map(doubleStrings, L))
