#CS 515
#Homework 2

negative_infinity = float('-inf')

def dot(L,K):
    '''
    The input of this function is: two lists, L and K.
    The dot product is only deﬁned for two lists of equal length.
    the function should return: the dot product of L and K,
    If the lengths of the lists are not equal, return negative inﬁnity,
    If these two lists are both empty, dot should output 0.0.
    '''
    if (L==[] and K==[]):
        combination = 0.0
        return combination
    # If these two lists are both empty, dot should output 0.0.
    elif (L[1:] == [] and K[1:] == []):
        dot_result = L[0] * K[0]
    # If these two lists gonna end next turn, the result would be return at this turn.
    elif (L[1:] == [] and K[1:] != []):
        return negative_infinity
    elif (L[1:] != [] and K[1:] == []):
        return negative_infinity
    # If the lengths of the lists are not equal, return negative infinity.
    else:
        dot_result = L[0] * K[0] + dot(L[1:], K[1:])
    return dot_result
    # the dot product of two vectors or lists is the sum of the products of the elements in the same position in the two vectors.

test1 = dot([5,3], [6,4])
print(test1)

def explode(S):
    '''
    The input of this function is: a  string
    the function should return: a list of all of the characters in the string.
    '''
    explode_result=[]
    if(S!=""):
    # If the given string not empty:
        explode_result.append(S[0])
        # first character.
        if(S[1:]!=""):
        # If the given string not end, do the recursion again.
            return explode(S[1:]) + explode_result
        else:
            return explode_result
        # If the given string end, return explode_result.

test22 = explode('spam')
print(test22)

def index(e,L):
    '''
    The input of this function is: an element e and a sequence L
    the function should return: the index at which e is first found in L.
    '''
    sequence_number=0
    if(e==L[0]):
        # If e is an element of L, return the index at which e is first found in L.
        return sequence_number
    else:
        sequence_number = sequence_number + 1
        # When e is not found yet, count + 1
        if(L[1:]==[]):
        # If e is NOT an element of L, then the function should return an integer that is equal to the length of L.
            return sequence_number
        else:
            sequence_number = sequence_number+index(e,L[1:])
            # If e is an element of L, do the recursion again.
            return sequence_number

test333 = index(42, range(0,100))
print(test333)

def deepReverse(L):
    '''
    The input of this function is: a list of elements L where some of the elements of the list may be lists themselves.
    the function should return: the reversal of the list where additionally, any elements within L that are also lists are deepReversed as well.
    '''
    def dR_tool(L, toollist):
        if L == []:
            return toollist
        elif isinstance(L[-1], list):
        # test whether or not an element in the list is a list itself.
            return dR_tool(L[:-1], toollist + [deepReverse(L[-1])])
        else:
            return dR_tool(L[:-1], toollist + [L[-1]])

    return dR_tool(L, [])

test4444 = deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]])
print(test4444)